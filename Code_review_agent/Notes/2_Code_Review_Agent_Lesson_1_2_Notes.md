# Code Review Agent --- Lesson 1 & Lesson 2 Notes

## Overview

We are building a **Code Review Agent**.

Its basic job is:

> Take source code → send it to an AI model → receive a review → produce
> structured findings.

The original project starts as a small Python program and gradually
evolves into a larger architecture with queues, workers, storage, and
testing.

---

# Lesson 1 --- Understand the System Before Architecture

## 1. What is the basic input and output?

### Input

The system receives **source code**.

Example:

```python
password = "admin123"
print(password)
```

### Output

The system produces **review findings**.

Example:

```json
[
  {
    "line": 1,
    "severity": "high",
    "message": "Hardcoded password detected."
  }
]
```

So the basic flow is:

```text
Source Code
    ↓
Review Engine
    ↓
Review Findings
```

---

## 2. What does the Review Engine do?

The review engine performs several steps:

```text
Source Code
    ↓
Create Prompt
    ↓
Create JSON Request
    ↓
HTTP POST
    ↓
Gemini
    ↓
HTTP Response
    ↓
Extract Model Text
    ↓
Parse JSON
    ↓
Structured Findings
```

In our current Python implementation, `review_code(code)` performs this
basic flow.

---

## 3. Our application and Gemini are different systems

Our Python application does not directly contain Gemini.

They are separate systems that communicate through the internet using
HTTP.

```text
Our Application
      │
      │ HTTP request
      ↓
    Gemini
      │
      │ HTTP response
      ↓
Our Application
```

This means our application is already communicating with an external
service.

---

## 4. What is an HTTP request doing here?

Our application sends something conceptually like:

```text
POST request
    ↓
Gemini API
    ↓
AI processes the prompt
    ↓
HTTP response
```

The request contains information such as:

- URL
- HTTP method
- JSON body
- Prompt/code to review

The response contains the model's result.

---

## 5. The first scalability problem

Suppose Gemini takes **10 seconds** to review one file.

With a simple synchronous design:

```text
User
  ↓
FastAPI
  ↓
Gemini
  ↓
wait 10 seconds
  ↓
Response
```

The HTTP request remains active while Gemini is working.

With many concurrent requests:

```text
User 1 → FastAPI → Gemini → waiting
User 2 → FastAPI → Gemini → waiting
User 3 → FastAPI → Gemini → waiting
...
User 1000
```

This can create problems involving:

- Long-running requests
- Server resources
- Concurrent workload
- AI provider limits

The important question is:

> Can our API layer safely handle the amount of expensive work being
> requested?

This leads to the next architectural improvement: **Queue + Worker**.

---

# Lesson 2 --- Queue + Worker Architecture

## 1. Why not let FastAPI perform the entire review?

The simple design is:

```text
User
  ↓
FastAPI
  ↓
Gemini
  ↓
Wait
  ↓
Response
```

This means FastAPI is responsible for both:

1. Receiving requests
2. Performing expensive AI processing

For a small number of requests this may be acceptable.

As concurrent workload increases, we want to separate these
responsibilities.

---

# 2. What is a Worker?

A **worker** is a separate process/service whose job is to:

1. Take a job
2. Perform the expensive work
3. Store/report the result
4. Take the next available job

For our application:

```text
Queue
  ↓
Worker
  ↓
Gemini
```

The worker consumes review jobs from the queue.

### Important terminology

```text
FastAPI → Producer
Worker  → Consumer
Queue   → Holds jobs between them
```

---

# 3. What is a Queue?

A **queue** is a place where jobs wait until a worker can process them.

Think about a restaurant:

```text
Customers
    ↓
Orders
    ↓
Kitchen Queue
    ↓
Chef
```

The same idea applies to our application:

```text
Users
  ↓
FastAPI
  ↓
Queue
  ↓
Worker
  ↓
Gemini
```

If many users submit reviews:

```text
             QUEUE
        ┌─────────────┐
        │ Review A    │
        │ Review B    │
        │ Review C    │
        │ Review D    │
        │ Review E    │
        └──────┬──────┘
               ↓
             Worker
```

The queue acts as a **buffer** between incoming requests and the workers
processing them.

---

# 4. Synchronous vs Asynchronous Job Processing

## Synchronous

The client waits for the operation to finish.

```text
Client
  ↓
FastAPI
  ↓
Gemini
  ↓
wait...
  ↓
Result
  ↓
Client
```

The HTTP request stays active while the expensive operation is running.

---

## Asynchronous job processing

The API accepts the job and returns without waiting for the expensive
operation to finish.

```text
Client
  ↓
FastAPI
  ↓
Queue
  ↓
"Job accepted / queued"
  ↓
Client
```

Separately:

```text
Queue
  ↓
Worker
  ↓
Gemini
  ↓
Result
```

The client can later check the job status.

Example:

```http
POST /reviews
```

Response:

```json
{
  "review_id": "abc123",
  "status": "queued"
}
```

Later:

```http
GET /reviews/abc123
```

Response:

```json
{
  "review_id": "abc123",
  "status": "completed",
  "findings": []
}
```

---

# 5. Important: Asynchronous does NOT mean Parallel

These concepts are related but different.

### Asynchronous

Means:

> The requester does not have to wait for the long-running operation to
> finish.

### Parallel / concurrent processing

Means:

> Multiple pieces of work can be processed at the same time.

For example, one worker can process jobs sequentially:

```text
Queue
  ↓
Worker
  ↓
Job A → Job B → Job C
```

Multiple workers can process several jobs concurrently:

```text
              Queue
          ┌─────┼─────┐
          ↓     ↓     ↓
         W1    W2    W3
```

Therefore:

```text
ASYNC ≠ PARALLEL
```

Remember this distinction.

---

# 6. First meaningful architecture

Our improved architecture becomes:

```text
                  USER
                    │
                    │ HTTP
                    ↓
             ┌──────────────┐
             │   FastAPI    │
             │     API      │
             └──────┬───────┘
                    │
                    │ create job
                    ↓
             ┌──────────────┐
             │    QUEUE     │
             └──────┬───────┘
                    │
                    │ consume job
                    ↓
             ┌──────────────┐
             │    WORKER    │
             └──────┬───────┘
                    │
                    │ HTTP
                    ↓
             ┌──────────────┐
             │    GEMINI    │
             └──────────────┘
```

This separates:

```text
API responsibility
        from
Review processing responsibility
```

---

# 7. Queue is a concept, not a specific technology

Do not think:

```text
Queue = Redis
```

Instead:

> A queue is an architectural concept. Redis is one technology that can
> implement a queue.

Examples of technologies that can provide queue/message-broker
functionality include:

- Redis
- RabbitMQ
- Amazon SQS
- Google Pub/Sub
- Azure Service Bus
- Kafka

The technology choice comes later.

---

# 8. The next architectural problem: large files

Suppose a user uploads:

```text
project.zip
50 MB
```

We should not normally put the entire 50 MB file directly into the
queue.

Instead:

```text
Large File
    ↓
Object/File Storage
    ↓
file_id / storage_key
    ↓
Queue
```

The queue should contain small job information such as:

```json
{
  "review_id": "abc123",
  "file_id": "file789"
}
```

The worker receives the identifier:

```text
Worker
  ↓
file_id = file789
  ↓
retrieve file from storage
  ↓
review file
```

So the general pattern is:

```text
Large data
    ↓
Storage

Small job information / reference
    ↓
Queue
```

This avoids unnecessarily moving large files through the queue.

---

# 9. Current architecture vs improved architecture

## Initial architecture

```text
User
  ↓
FastAPI
  ↓
Gemini
  ↓
Response
```

Problem:

```text
FastAPI request
      ↓
wait for expensive AI work
      ↓
response
```

## Improved architecture

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

Now the API can accept the job and the worker can process it
independently.

---

# 10. Key terms to remember

---

  Term                                Simple meaning

---

  **API**                             Interface through which clients
                                      communicate with our application

  **FastAPI**                         Framework we use to build the API

  **HTTP**                            Communication protocol used between
                                      systems

  **Gemini**                          External AI service that reviews
                                      the code

  **Job**                             A unit of work that needs to be
                                      processed

  **Queue**                           Holds jobs until workers process
                                      them

  **Worker**                          Processes jobs from the queue

  **Producer**                        Component that adds jobs to the
                                      queue

  **Consumer**                        Component that takes jobs from the
                                      queue

  **Synchronous**                     Client waits for the operation to
                                      finish

  **Asynchronous job processing**     Client does not wait for the
                                      long-running operation

**Storage**                         Place where large files/data are
                                      stored
--------------------------------------------

---

# 11. The mental model

Remember this simple picture:

```text
USER
  │
  │ request
  ↓
FASTAPI
  │
  │ create job
  ↓
QUEUE
  │
  │ consume job
  ↓
WORKER
  │
  │ request
  ↓
GEMINI
  │
  │ result
  ↓
STORAGE / DATABASE
```

The main idea is:

> **FastAPI receives the work. The queue holds the work. The worker
> performs the work. Gemini performs the AI part. Storage holds large
> data/results.**

---

# Lesson 1 + Lesson 2 --- What you should know

Before moving forward, you should be able to explain these without
memorizing definitions:

1. What is the input and output of our Code Review Agent?
2. Why does our application communicate with Gemini using HTTP?
3. Why can long Gemini processing become a problem for the API?
4. What is a worker?
5. What is a queue?
6. Why do we separate FastAPI from the worker?
7. What is synchronous processing?
8. What is asynchronous job processing?
9. Why is asynchronous processing not automatically parallel
   processing?
10. Why should large files go to storage instead of directly into the
    queue?
11. What is the difference between a producer and a consumer?

---

# One-line summary

```text
Lesson 1:
Understand what the Code Review Agent does.

Lesson 2:
Separate request handling from expensive processing using:

FastAPI → Queue → Worker → Gemini
```

The next architectural question is:

> **Where exactly are the uploaded files stored, how does the worker
> retrieve them, and where should the review result be stored?**
