# AI Code Review Agent — Project Flow

```text
                    ┌──────────────────────┐
                    │       CLIENT         │
                    │  Sends source_code   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI API     │
                    │     POST /reviews    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Create ReviewJob  │
                    │                      │
                    │ status = "queued"    │
                    │ attempts = 0         │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌──────────────────┐
        │   PostgreSQL    │        │  Local Storage   │
        │                 │        │                  │
        │ ReviewJob       │        │ reviews/{id}/    │
        │ id              │        │ source.py        │
        │ status          │        │                  │
        │ source_location │        └──────────────────┘
        │ attempts        │
        └─────────────────┘
                 │
                 │ job.id
                 ▼
        ┌──────────────────────┐
        │        Redis         │
        │    review_queue      │
        │                      │
        │       [Job ID]       │
        └──────────┬───────────┘
                   │
                   │ BRPOPLPUSH
                   ▼
        ┌──────────────────────┐
        │       Worker         │
        │                      │
        │ review_queue         │
        │        ↓             │
        │ processing_queue     │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │     PostgreSQL       │
        │                      │
        │ Find ReviewJob       │
        │ status → processing  │
        │ attempts += 1        │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │    Local Storage     │
        │                      │
        │ Read source.py       │
        └──────────┬───────────┘
                   │
                   │ source code
                   ▼
        ┌──────────────────────┐
        │      AI Service      │
        │                      │
        │ Gemini API           │
        │                      │
        │ Code → Prompt → AI   │
        └──────────┬───────────┘
                   │
                   ▼
             ┌─────────────┐
             │   Success?  │
             └──────┬──────┘
                YES │       │ NO
                    │       │
                    ▼       ▼
        ┌────────────────┐  ┌──────────────────┐
        │ Store findings │  │ Retryable error? │
        │                │  └────────┬─────────┘
        │ status=        │       YES │       │ NO
        │ "completed"    │           │       │
        └───────┬────────┘           ▼       ▼
                │             ┌──────────┐ ┌──────────┐
                │             │ Retry    │ │ Failed   │
                │             │ max 3    │ │          │
                │             │ attempts │ │ status = │
                │             └────┬─────┘ │ "failed" │
                │                  │       └──────────┘
                │                  │
                │                  ▼
                │             ┌──────────┐
                │             │ Backoff  │
                │             │ 2^n sec  │
                │             └────┬─────┘
                │                  │
                │                  ▼
                │             Redis Queue
                │             again
                │
                ▼
        ┌──────────────────────┐
        │         ACK          │
        │                      │
        │ Remove from          │
        │ processing_queue     │
        │                      │
        │ Remove from          │
        │ processing_jobs      │
        └──────────────────────┘
```

## Flow Summary

1. **Client** sends `source_code` to `POST /reviews`.
2. **FastAPI** creates a `ReviewJob`.
3. The job is initially marked as **`queued`**.
4. Job metadata is stored in **PostgreSQL**.
5. Source code is saved in **Local Storage** as `reviews/{id}/source.py`.
6. The job ID is pushed into the **Redis `review_queue`**.
7. The **Worker** takes the job using `BRPOPLPUSH`.
8. The job moves from `review_queue` to `processing_queue`.
9. The worker loads the job from **PostgreSQL** and changes its status to **`processing`**.
10. The worker reads the source code from **Local Storage**.
11. The source code is sent to the **Gemini AI Service** for review.
12. If successful, findings are stored and the job becomes **`completed`**.
13. The worker **ACKs** the job by removing it from the processing structures.
14. If a retryable error occurs, the worker retries up to **3 attempts** using exponential backoff.
15. If the maximum retry count is reached, the job becomes **`failed`**.
