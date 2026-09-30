# Code Review System — Complete Flow Diagram

```text
                              100 USERS
                                  │
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ↓                           ↓
              User 1 Request              User 2 Request
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                ...
                                  │
                                  ↓
                           User 100 Request
                                  │
                                  │
                                  ▼
                    ╔═══════════════════════╗
                    ║       FASTAPI         ║
                    ║     API SERVER        ║
                    ╚═══════════╤═══════════╝
                                │
                 ┌──────────────┼───────────────┐
                 │              │               │
                 │              │               │
                 ▼              ▼               ▼
             Create Job     Store Metadata   Store File
             / Job ID       PostgreSQL       Object Storage
                 │              │               │
                 │              │               │
                 │              ▼               ▼
                 │         ┌──────────┐   ┌─────────────┐
                 │         │PostgreSQL│   │   Object    │
                 │         │          │   │   Storage   │
                 │         │job_id    │   │             │
                 │         │user_id   │   │ code.zip    │
                 │         │file_id   │   │ source.py   │
                 │         │status    │   │ repository  │
                 │         └────┬─────┘   └──────┬──────┘
                 │              │                │
                 │              │                │
                 └──────────────┼────────────────┘
                                │
                                ▼
                         Put small job
                         message into
                            QUEUE
                                │
                                ▼
                    ╔═══════════════════════╗
                    ║         QUEUE         ║
                    ║                       ║
                    ║ Job 101               ║
                    ║ Job 102               ║
                    ║ Job 103               ║
                    ║ Job 104               ║
                    ║ ...                   ║
                    ║ Job 200               ║
                    ╚═══════════╤═══════════╝
                                │
                                │
                         Workers consume
                              jobs
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
          ╔══════════╗    ╔══════════╗     ╔══════════╗
          ║ Worker 1 ║    ║ Worker 2 ║     ║ Worker 3 ║
          ╚════╤═════╝    ╚════╤═════╝     ╚════╤═════╝
               │               │                │
               │               │                │
               └───────────────┼────────────────┘
                               │
                               ▼
                       PROCESS THE JOB
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             PostgreSQL             Object Storage
             get job info           get actual code
                    │                     │
                    │                     │
                    └──────────┬──────────┘
                               │
                               ▼
                         Worker has:
                         ┌─────────────┐
                         │ Job ID      │
                         │ User ID     │
                         │ Source Code │
                         │ Other info  │
                         └──────┬──────┘
                                │
                                ▼
                         Call Gemini API
                                │
                                ▼
                       ╔════════════════╗
                       ║     GEMINI     ║
                       ║   AI MODEL     ║
                       ╚═══════╤════════╝
                               │
                               │ Review result
                               ▼
                         Worker receives
                            response
                               │
                               ▼
                       Parse / Validate
                         AI response
                               │
                               ▼
                       Store final result
                         PostgreSQL
                               │
                               ▼
                    status = "completed"
                               │
                               │
                               ▼
                         USER CHECKS
                         JOB STATUS
                               │
                               ▼
                     GET /reviews/{id}
                               │
                               ▼
                         FastAPI reads
                          PostgreSQL
                               │
                               ▼
                         Return result
                               │
                               ▼
                             USER
```
