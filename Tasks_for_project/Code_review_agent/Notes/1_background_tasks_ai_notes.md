# Background Tasks in AI — Learning Notes

## 1. Synchronous vs Background Processing

### Synchronous

The client waits while the server processes the work.

```text
Client
  ↓ request
Server
  ↓
process
  ↓
wait...
  ↓
response
```

Mental model:

> Do the work now, then give me the answer.

### Asynchronous / Background

The client gets an immediate response that the work has started, while the actual work continues separately.

```text
Client
  ↓ request
Server
  ↓
"Job started"
  ↓
Client can continue

Background
  ↓
process
  ↓
finished
  ↓
result stored
```

Important:

> Asynchronous does not automatically mean background task. Background processing is one way to perform work without making the original request wait.

---

## 2. Why Background Processing Is Useful for AI

AI requests can sometimes take a long time.

Example:

```text
POST /review
     ↓
call Gemini
     ↓
wait 40 seconds
     ↓
response
```

Instead:

```text
POST /review
     ↓
create review job
     ↓
return job_id
```

The long-running work happens separately:

```text
Background job
      ↓
call Gemini
      ↓
wait 40 seconds
      ↓
save result
```

Important:

> A background job does not make Gemini respond faster. It prevents the original API request from having to wait for the long-running work.

---

# 3. What Is a Job?

A **job** represents a piece of work that needs to be completed.

Example:

```text
Job #123

Task:
Review this Python file

Status:
processing
```

A job needs an identity so the application can track that particular piece of work.

## Why do we need a job_id?

Multiple users can submit work:

```text
Client A → Job #101
Client B → Job #102
Client C → Job #103
```

The server can track each job independently.

The important distinction:

> A job_id identifies the particular piece of work. It does not necessarily identify the client by itself.

The application can maintain a relationship such as:

```text
job_id → user/client → task → status → result
```

---

# 4. Job Lifecycle

A job moves through states.

```text
             CREATE
               │
               ▼
          ┌──────────┐
          │ PENDING  │
          └────┬─────┘
               │
               ▼
         ┌────────────┐
         │ PROCESSING │
         └─────┬──────┘
               │
          ┌────┴────┐
          ▼         ▼
     COMPLETED     FAILED
```

### PENDING

The job exists, but processing has not started yet.

### PROCESSING

A worker is currently doing the work.

### COMPLETED

The work finished successfully.

### FAILED

Something went wrong.

Example:

```json
{
  "job_id": 123,
  "status": "processing"
}
```

Later:

```json
{
  "job_id": 123,
  "status": "completed",
  "result": [...]
}
```

Or:

```json
{
  "job_id": 123,
  "status": "failed",
  "error": "Gemini request timed out"
}
```

---

# 5. What Is a Worker?

A **worker** is a program/process whose job is to take a job and actually perform the work.

For an AI code-review job:

```text
Worker
  ↓
Find Job #101
  ↓
Read the code
  ↓
Call Gemini
  ↓
Wait for Gemini
  ↓
Receive result
  ↓
Save result
  ↓
Mark Job #101 = completed
```

Why separate the worker from the API?

Without a worker:

```text
API
 │
 ├── receive request
 ├── call Gemini
 ├── wait 40 sec
 └── return response
```

With a worker:

```text
API
 │
 ├── receive request
 ├── create job
 └── return job_id
       │
       ▼
     Worker
       │
       ├── call Gemini
       ├── wait
       ├── process result
       └── save result
```

The API can continue serving other requests.

---

# 6. What Is a Queue?

A **queue** is a waiting line for work.

Example:

```text
              QUEUE
        ┌────────────────┐
        │ Job 101        │
        │ Job 102        │
        │ Job 103        │
        │ Job 104        │
        │ Job 105        │
        └────────────────┘
                 │
                 ▼
              Worker
```

The worker takes jobs from the queue.

## Why do we need a queue?

Suppose 100 users submit code reviews but there are only 3 workers:

```text
                    QUEUE
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Worker 1     Worker 2     Worker 3
        │            │            │
      Gemini       Gemini       Gemini
```

The other jobs wait in the queue until a worker becomes available.

So:

```text
PENDING
  ↓
waiting in queue for a worker

PROCESSING
  ↓
worker has picked it up and is doing the work
```

This is also a way to control concurrency.

---

# 7. Queue vs Database

These are different concepts.

### Queue

> What work needs to be done?

```text
Job 101
Job 102
Job 103
```

### Database

> What is the current state/result of the work?

```text
101 → completed
102 → processing
103 → pending
```

### Worker

> Who actually performs the work?

```text
Worker → Gemini
```

Do not mix these concepts.

---

# 8. Why Store Jobs in a Database?

Suppose job information exists only in application memory:

```text
Job #101 → processing
```

If the server crashes and restarts:

```text
Server restart
      ↓
Job #101
❌ Gone
```

A persistent database can retain information such as:

- job status
- job result
- failure information
- timestamps
- retry information

Conceptually:

```text
jobs
------------------------------------------------
id       status       result       created_at
------------------------------------------------
101      completed    [...]        10:30
102      processing   NULL         10:31
103      pending      NULL         10:32
104      failed       NULL         10:33
```

---

# 9. Complete Mental Model

The full architecture we have learned so far:

```text
                         USER
                           │
                           ▼
                          API
                           │
                    Create Job #101
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
           DATABASE                 QUEUE
        status=pending                │
                                      ▼
                                   WORKER
                                      │
                                      ▼
                                    GEMINI
                                      │
                                      ▼
                                   RESULT
                                      │
                                      ▼
                                  DATABASE
                              status=completed
                              result=[...]
                                      │
                                      ▼
                                     API
                                      │
                                      ▼
                                    USER
```

## The four core components

```text
API     → accepts the request

Job     → represents the work

Queue   → holds work waiting to be processed

Worker  → performs the work
```

And the database keeps the job's persistent state and result.

---

# 10. Code-Review Agent Example

Eventually, the AI code-review flow can look like:

```text
User
  ↓
POST /review
  ↓
Create Job
  ↓
Return job_id immediately
  ↓
Queue
  ↓
Worker
  ↓
Gemini
  ↓
Findings
  ↓
Save result
  ↓
GET /review/{job_id}
  ↓
User receives result
```

This solves the specific problem of a long-running Gemini request keeping the original API request waiting.

---

# 11. Important Distinctions to Remember

### Timeout

A timeout means:

> Our application stopped waiting for the operation within its configured time limit.

It does not automatically mean Gemini's server failed.

### Background task

A background task means:

> The long-running work is performed separately from the original request.

### Job

A job is:

> A specific piece of work that can be tracked.

### Queue

A queue is:

> A place where work waits to be processed.

### Worker

A worker is:

> The process that actually performs the work.

### Database

A database is:

> Persistent storage for the job's state, result, errors, and related information.

---

# Current Learning Progress

We have learned:

1. Synchronous processing
2. Asynchronous/background processing
3. What a job is
4. Why job_id is needed
5. Job lifecycle
6. What a worker is
7. What a queue is
8. Why queues are useful
9. Queue vs database
10. Why job state should be persistent
11. The complete API → Job → Queue → Worker → Gemini flow

## Next Topic

**Failure and reliability:**

```text
Worker
  ↓
Gemini
  ↓
FAIL
```

We will learn:

- What happens when a worker fails
- What happens when Gemini times out
- Retry
- Failed jobs
- Why we should not retry forever
- What happens if a worker crashes halfway through a job
