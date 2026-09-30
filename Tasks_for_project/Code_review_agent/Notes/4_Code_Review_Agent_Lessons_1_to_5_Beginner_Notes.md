# Code Review Agent — Lessons 1–5

> **Goal:** Understand the architecture and reliability model before writing the production implementation.

---

# Lesson 1 — Basic System

## What does the system do?

```text
Source Code
    ↓
Review Engine
    ↓
Gemini
    ↓
Structured Findings
```

- **Input:** source code
- **Output:** structured review findings
- **Gemini:** external AI service
- **HTTP:** communication between our application and Gemini

### Basic problem

If Gemini takes a long time, the API request stays active:

```text
User → FastAPI → Gemini → WAIT → Response
```

With many concurrent requests, many API requests can be waiting.

---

# Lesson 2 — Queue + Worker

## Why?

Separate **receiving requests** from **expensive processing**.

```text
User
  ↓
FastAPI
  ↓
Queue
  ↓
Worker
  ↓
Gemini
```

### Responsibilities

| Component | Responsibility                   |
| --------- | -------------------------------- |
| FastAPI   | Receive requests and create jobs |
| Queue     | Hold jobs waiting for processing |
| Worker    | Process jobs                     |
| Gemini    | Analyze code                     |

---

## Asynchronous processing

The client does **not** wait for the long-running review.

```text
Client
  ↓
FastAPI
  ↓
Queue
  ↓
"Queued"
  ↓
Client
```

Later:

```text
Queue → Worker → Gemini → Result
```

### Important

**Async ≠ Parallel**

- Async: requester does not wait for the long operation.
- Concurrent/parallel processing: multiple jobs can be processed at the same time.
- One worker can process jobs sequentially.
- Multiple workers can process multiple jobs concurrently.

---

## Large files

Do not put large source files directly into the queue.

```text
Large File
    ↓
Object Storage
```

Put a small reference in the queue:

```json
{
  "job_id": "123",
  "file_id": "abc"
}
```

Then the worker retrieves the actual file from storage.

---

# Lesson 3 — Complete Data Flow

For many users:

```text
Users
  ↓
FastAPI
  ├── Create job_id
  ├── Store metadata → PostgreSQL
  ├── Store file → Object Storage
  └── Put job message → Queue
                         ↓
                       Worker
                         ↓
                 Get job + file
                         ↓
                      Gemini
                         ↓
                 Store result
                         ↓
                    PostgreSQL
```

### The four important separations

```text
PostgreSQL
→ What is the job's state?

Object Storage
→ Where is the actual code/file?

Queue
→ What work needs to be processed?

Worker
→ Who performs the work?
```

---

# Lesson 4 — What happens inside a Queue?

A queue such as Redis is a **separate service**.

```text
FastAPI
   │
   ↓
 Redis Queue
   │
   ↓
 Worker
```

FastAPI and the worker do **not** share Python memory.

### Producer and Consumer

```text
FastAPI → Producer
Worker  → Consumer
```

Example:

```text
Queue
────────────
Job 101
Job 102
Job 103
```

Worker takes a job:

```text
Queue → Worker → Process Job
```

---

## ACK

**ACK = acknowledgement**

It means:

> "I successfully processed this job."

Conceptually:

```text
Job
 ↓
Worker receives it
 ↓
Worker processes it
 ↓
Worker sends ACK
 ↓
Job is considered successfully handled
```

If the worker crashes before ACK:

```text
Job
 ↓
Worker
 ↓
💥
 ↓
No ACK
 ↓
Retry
```

### Important

The queue usually does not literally know:

> "The worker crashed."

It knows:

> **"The expected acknowledgement did not arrive within the allowed time."**

---

# Lesson 5 — Retry, Duplicate Jobs & Idempotency

## The dangerous case

Worker 1 may process a job but fail before ACK:

```text
Worker 1
   ↓
Process Job
   ↓
Save result
   ↓
💥 Crash
   ↓
No ACK
```

The queue may retry the job:

```text
Job
 ↓
Worker 2
```

Now the same job was executed twice.

---

## Why duplicates are dangerous

Without protection:

```text
Worker 1 → save result
Worker 2 → save result again
```

This can create duplicate results or repeated side effects.

Therefore:

> **Assume a job may be processed more than once.**

---

## Idempotency

**Idempotency** means:

> Processing the same job multiple times should still leave the system in the correct final state.

Use the unique `job_id` / `review_id` to identify the operation.

Example:

```text
Worker 2
   ↓
Check job state
   ↓
Already completed?
   ↓
Yes → Do not process again
   ↓
ACK
```

---

## Race condition

Two workers may receive the same job at nearly the same time:

```text
             Job 123
              /   \
             ↓     ↓
        Worker 1  Worker 2
```

Both might see:

```text
status = queued
```

and both try to process it.

### Solution: atomic claim

Conceptually:

```sql
UPDATE reviews
SET status = 'processing'
WHERE job_id = 123
  AND status = 'queued';
```

If:

```text
1 row changed → job claimed
0 rows changed → someone else already claimed it
```

This prevents both workers from claiming the same job.

---

## Worker crash after claiming

Another problem:

```text
queued
  ↓
processing
  ↓
Worker crashes
```

The job must not remain `processing` forever.

Use a **lease / timeout / heartbeat** concept.

```text
Worker claims job
      ↓
Lease is valid
      ↓
Worker sends heartbeat / renews lease
      ↓
Worker finishes → ACK
```

If the worker dies:

```text
No heartbeat
      ↓
Lease expires
      ↓
Job can be retried/reclaimed
```

---

# Master Mental Model

```text
                         USER
                           │
                           ↓
                        FASTAPI
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
         PostgreSQL   Object Storage   Queue
         metadata         files          │
                                          ↓
                                       Worker
                                          │
                                  ┌───────┴───────┐
                                  ↓               ↓
                             Get metadata     Get file
                                  │               │
                                  └───────┬───────┘
                                          ↓
                                        Gemini
                                          │
                                          ↓
                                    Save result
                                          │
                                          ↓
                                     PostgreSQL
                                          │
                                          ↓
                                         ACK
```

## Reliability flow

```text
Queue
  ↓
Worker
  ↓
Claim
  ↓
Process
  ↓
Save result
  ↓
ACK
```

If something goes wrong:

```text
Worker fails
    ↓
No ACK / lease expires
    ↓
Retry
    ↓
Another worker
    ↓
Idempotency + atomic claim
    ↓
Correct final result
```

---

# 10 Things to Remember

1. **FastAPI** receives requests.
2. **Gemini** performs AI analysis.
3. **Queue** holds work waiting to be processed.
4. **Worker** performs background work.
5. **PostgreSQL** stores structured state/metadata/results.
6. **Object Storage** stores large files.
7. **Async** means the requester does not wait for the long operation.
8. **Async ≠ parallel.**
9. **ACK + retry** helps prevent lost work.
10. **Idempotency + atomic claiming + lease/timeout** help handle duplicate and failed processing.

## One-line mental model

> **FastAPI receives → Storage stores → Queue waits → Worker processes → Gemini analyzes → PostgreSQL records → ACK confirms.**
