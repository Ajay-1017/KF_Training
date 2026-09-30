# Code Review System --- Queue & Redis Architecture Notes

## 1. The Complete Flow

```text
                              USER
                                │
                                │ Upload Python code
                                ▼
                     ┌─────────────────────┐
                     │       FastAPI       │
                     │     API Server      │
                     └──────────┬──────────┘
                                │
                    1. Receive request
                    2. Create review_id
                    3. Store review metadata
                    4. Store actual file
                    5. Put small job message in queue
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
        ┌──────────────┐ ┌──────────────┐ ┌────────────────┐
        │ PostgreSQL   │ │Object Storage│ │ Redis Server   │
        │              │ │              │ │                │
        │ review_id    │ │ Actual code  │ │ review_queue   │
        │ user_id      │ │ source file  │ │                │
        │ status       │ │              │ │ [job-101]      │
        │ file_id      │ │              │ │ [job-102]      │
        │ timestamps   │ │              │ │ [job-103]      │
        └──────────────┘ └──────────────┘ └───────┬────────┘
                                                  │
                                          Job is waiting
                                                  │
                                                  ▼
                                      ┌────────────────────┐
                                      │      Worker 1      │
                                      │      Worker 2      │
                                      │      Worker 3      │
                                      └─────────┬──────────┘
                                                │
                                      Get review_id
                                                │
                                                ▼
                                         PostgreSQL
                                                │
                                      Claim/check job state
                                                │
                                                ▼
                                         Object Storage
                                                │
                                      Download actual code
                                                │
                                                ▼
                                            Gemini
                                                │
                                      AI code review
                                                │
                                                ▼
                                            Worker
                                                │
                                      Save review result
                                                │
                                                ▼
                                         PostgreSQL
                                                │
                                      status = completed
                                                │
                                                ▼
                                             Redis
                                                │
                                               ACK
                                                │
                                                ▼
                                               DONE
```

---

# 2. Why Did We Introduce a Queue?

The original design is:

```text
User
  ↓
FastAPI
  ↓
Gemini
  ↓
Response
```

This is simple, but Gemini is a relatively slow external operation.

If many users arrive:

```text
100 requests
     ↓
   FastAPI
     ↓
   Gemini
     ↓
   Wait...
```

FastAPI has to deal with many long-running operations.

The fundamental problem is:

```text
Incoming work rate
        ≠
Processing rate
```

Example:

```text
Incoming jobs   = 100 / second
Processing      = 20 / second
```

We need somewhere to hold the jobs that are waiting.

That is the role of a **queue**.

---

# 3. Why Not Keep the Queue Inside FastAPI?

A simple implementation might be:

```python
queue = []
```

But this queue belongs to the memory of that Python process.

### Problem 1 --- FastAPI crashes

```text
FastAPI
   │
   └── Python memory
        ├── job-101
        ├── job-102
        └── job-103

FastAPI crashes
      ↓
Process memory disappears
      ↓
Queued jobs may disappear
```

### Problem 2 --- Multiple FastAPI instances

Enterprise applications may have:

```text
                 Load Balancer
                 /     |     \
                /      |      \
          FastAPI 1 FastAPI 2 FastAPI 3
             │         │         │
           Queue A   Queue B   Queue C
```

We want one shared queue instead:

```text
FastAPI 1 ──┐
FastAPI 2 ──┼──► Shared Queue ◄── Workers
FastAPI 3 ──┘
```

Therefore, the queue should be a **separate service**.

---

# 4. Why Redis?

We need a system that can:

- receive jobs from multiple application instances
- hold waiting jobs
- allow workers to consume jobs
- operate very quickly
- exist independently of FastAPI's process memory

Redis is one technology that can provide this.

Other technologies can also provide queue/message functionality:

```text
Redis
RabbitMQ
Amazon SQS
Kafka
Google Pub/Sub
Azure Service Bus
```

For our learning architecture:

```text
FastAPI → Redis → Workers
```

Redis was not created specifically for our code-review application.

Rather:

```text
Need shared fast data/message coordination
              ↓
           Redis
              ↓
Use Redis data structures for queueing
```

---

# 5. What Exactly Is Redis?

Redis is a **separate server/process** that primarily maintains data in
memory and provides fast operations on data structures.

It is not simply a Python library.

A simplified local setup could look like:

```text
Computer / Server
│
├── FastAPI process
│
├── Worker process
│
└── Redis process
```

In production, Redis can run as a separate server or managed service:

```text
Application Servers
        │
        │ Network
        ▼
   Redis Server
        │
        │ Network
        ▼
   Worker Servers
```

---

# 6. How Does FastAPI Connect to Redis?

FastAPI uses a Redis client library.

Conceptually:

```text
┌──────────────┐
│   FastAPI    │
│   Python     │
└──────┬───────┘
       │
       │ Redis client
       │
       │ Network connection
       ▼
┌──────────────┐
│ Redis Server │
│              │
│ Port: 6379   │
└──────────────┘
```

The Python Redis client is **not the queue**.

It is the interface that allows Python to communicate with the Redis
server.

The worker uses the same idea:

```text
┌──────────────┐
│    Worker    │
│    Python    │
└──────┬───────┘
       │
       │ Redis client
       │
       ▼
┌──────────────┐
│ Redis Server │
└──────────────┘
```

FastAPI and the worker communicate through Redis rather than directly
communicating with each other.

---

# 7. What Does Redis Actually Maintain?

Redis fundamentally maintains mappings between:

```text
KEY → VALUE / DATA STRUCTURE
```

For our queue, conceptually:

```text
"review_queue"
       │
       ▼
 Redis data structure
       │
       ├── job-101
       ├── job-102
       └── job-103
```

Important:

> Redis does not inherently know that the name `review_queue` means
> "queue".

The name is simply a Redis key.

For example, you could call the key:

```text
banana
```

The name does not matter.

The operation and data structure determine how it is used.

---

# 8. How Does Our Queue Become a Redis Queue?

Suppose FastAPI wants to add:

```text
job-101
```

Conceptually it sends:

```text
RPUSH review_queue job-101
```

Redis does approximately:

```text
Receive command
      ↓
Find key "review_queue"
      ↓
Find the data structure associated with that key
      ↓
Add job-101 to the structure
      ↓
Return result
```

After several jobs:

```text
"review_queue"
       │
       ▼
┌────────────┬────────────┬────────────┐
│ job-101    │ job-102    │ job-103    │
└────────────┴────────────┴────────────┘
```

For a simple Redis List-based queue, the list is the data structure
being used.

---

# 9. How Does the Worker Get a Job?

The worker can request a job conceptually using:

```text
BLPOP review_queue
```

Redis:

```text
Find "review_queue"
        ↓
Find its data structure
        ↓
Take the next job
        ↓
Return it to worker
```

Conceptually:

```text
Redis
  │
  │ [job-101][job-102][job-103]
  │
  │ BLPOP
  ▼
Worker receives job-101
```

The queue structure is then conceptually:

```text
[job-102][job-103]
```

---

# 10. Why Does the Worker Use a Blocking Operation?

If there are no jobs:

```text
review_queue
     ↓
   empty
```

A worker should not continuously do:

```text
"Any job?"
"Any job?"
"Any job?"
"Any job?"
```

That wastes resources.

A blocking operation lets the worker effectively wait:

```text
Worker
   │
   │ "Give me a job"
   ▼
Redis
   │
   │ No job
   │
   │ WAIT
   │
   │ New job arrives
   ▼
Worker receives job
```

This is much more efficient than constantly polling.

---

# 11. Where Is the Queue Memory Maintained?

The active Redis data is primarily maintained in:

```text
RAM of the Redis server
```

Conceptually:

```text
Redis Server
│
└── RAM
     │
     ├── "review_queue"
     │       │
     │       ├── job-101
     │       ├── job-102
     │       └── job-103
     │
     └── Other Redis data
```

Therefore:

- FastAPI does not own the queue memory.
- Worker does not own the queue memory.
- Redis owns and manages the active queue data.

The simplest mental model is:

> **Redis server owns the memory; the queue is a data structure
> maintained inside that Redis memory.**

---

# 12. What Happens When FastAPI Sends a Job?

Complete small flow:

```text
FastAPI
   │
   │ 1. Create review_id
   │
   │ 2. Store metadata in PostgreSQL
   │
   │ 3. Store actual source code in Object Storage
   │
   │ 4. Send review_id to Redis
   ▼
Redis
   │
   │ "review_queue"
   │
   └── [review-101]
```

The queue should normally contain a **small job reference**, not the
entire source file.

Example:

```json
{
  "review_id": "review-101"
}
```

The actual source code remains in object storage.

---

# 13. Why Keep the Actual File Outside Redis?

Suppose the uploaded code file is large.

We do not want:

```text
Redis
└── huge source file
```

Instead:

```text
Redis
└── review-101

PostgreSQL
└── review-101 → storage_key

Object Storage
└── actual source file
```

The worker can then:

```text
review_id
   ↓
PostgreSQL
   ↓
storage_key
   ↓
Object Storage
   ↓
actual code
```

---

# 14. What Happens With Multiple Workers?

Suppose:

```text
Redis Queue

[job-101][job-102][job-103][job-104]
```

Workers:

```text
       Redis
      /  |  \
     /   |   \
   W1    W2    W3
```

Jobs can be distributed among workers:

```text
job-101 → W1
job-102 → W2
job-103 → W3
job-104 → available worker
```

This gives us concurrent background processing.

---

# 15. What If FastAPI's Redis Connection Breaks?

Important distinction:

```text
FastAPI ──X── Redis
```

If only the connection fails:

```text
FastAPI connection → ❌
Redis server       → ✅
```

Data already maintained by Redis normally remains in Redis memory.

The connection failure itself does not delete Redis's data.

---

# 16. What If Redis Itself Crashes?

Different situation:

```text
Redis server 💥
```

The active data is in RAM, so RAM data can be lost depending on the
failure and configuration.

Redis provides persistence mechanisms such as:

```text
RDB
AOF
```

which can be used for recovery.

Production deployments can also use replication/failover for higher
availability.

So:

```text
Active queue
    ↓
Redis RAM

Recovery protection
    ↓
Persistence
    +
Replication / Failover
```

---

# 17. PostgreSQL vs Redis

These two have different responsibilities.

### PostgreSQL

Answers:

> "What is the durable business state of this review?"

Example:

```text
review_id = 101
status = processing
user_id = 25
file_id = abc123
created_at = ...
```

### Redis

Answers:

> "What work is waiting / being coordinated for processing?"

Example:

```text
review_queue
   ↓
job-101
job-102
job-103
```

Therefore:

```text
PostgreSQL → durable business state
Redis      → fast queue/coordination
```

---

# 18. Complete Enterprise-Level Mental Model

```text
                              USER
                                │
                                │ Upload code
                                ▼
                     ┌─────────────────────┐
                     │       FastAPI       │
                     │     API Servers     │
                     └──────────┬──────────┘
                                │
                    ┌───────────┼────────────┐
                    │           │            │
                    ▼           ▼            ▼
              PostgreSQL   Object Storage   Redis
                    │           │            │
                    │           │            │
                    │           │       review_queue
                    │           │       ┌───────────┐
                    │           │       │ job-101   │
                    │           │       │ job-102   │
                    │           │       │ job-103   │
                    │           │       └─────┬─────┘
                    │           │             │
                    │           │             │
                    │           │       ┌─────┴──────┐
                    │           │       │            │
                    │           │       ▼            ▼
                    │           │     Worker 1     Worker 2
                    │           │       │            │
                    │           │       └──────┬─────┘
                    │           │              │
                    │           │              ▼
                    │           │       Check/claim job
                    │           │              │
                    │           │              ▼
                    │           └──────► Object Storage
                    │                          │
                    │                          ▼
                    │                        Code
                    │                          │
                    │                          ▼
                    │                        Gemini
                    │                          │
                    │                          ▼
                    │                     Review result
                    │                          │
                    ◄──────────────────────────┘
                    │
                    ▼
             Update PostgreSQL
             status = completed
                    │
                    ▼
                  ACK
                    │
                    ▼
              Queue considers
              message processed
```

---

# 19. The Complete Reasoning Chain

Remember this sequence rather than memorizing Redis definitions:

```text
Gemini processing takes time
        ↓
Don't make every API request wait
        ↓
Use background workers
        ↓
Workers need jobs
        ↓
Need a queue
        ↓
Queue shouldn't live in FastAPI process memory
        ↓
Need a separate shared queue service
        ↓
Redis can provide this
        ↓
Redis maintains data structures in its server memory
        ↓
A Redis key identifies our queue structure
        ↓
Jobs are stored in that structure
        ↓
FastAPI adds jobs
        ↓
Workers consume jobs
```

## One sentence to remember

> **FastAPI produces jobs, Redis maintains the shared queue in its own
> memory, workers consume the jobs, PostgreSQL maintains durable
> business state, Object Storage maintains large files, and Gemini
> performs the actual AI work.**
