
# FastAPI + Uvicorn Request Lifecycle (Mental Model)

```text
                     START SERVER
                          │
                          ▼
                uvicorn main:app
                          │
                          ▼
          Creates Worker Process (1 Worker)
                          │
                          ▼
                Creates Main Thread
                          │
                          ▼
          Starts asyncio Event Loop
                          │
                          ▼
        Server waits continuously for HTTP requests

══════════════════════════════════════════════════════════════════════

                  CLIENT SENDS REQUEST
                          │
                          ▼
              Uvicorn receives HTTP request
                          │
                          ▼
          Passes request to FastAPI application
                          │
                          ▼
       FastAPI + Starlette performs route matching
                          │
              ┌───────────┴────────────┐
              │                        │
         Route Not Found          Route Found
              │                        │
              ▼                        ▼
         Return 404            Resolve Dependencies
                                    │
                                    ▼
                    Create required objects
               (AsyncSession, User, etc.)
                                    │
                                    ▼
                 Is the endpoint async?
                    ┌────────┴────────┐
                    │                 │
                  YES               NO
                    │                 │
                    ▼                 ▼
          Create Coroutine      Normal Function
               Object                 │
                    │                 │
                    ▼                 ▼
          Event Loop executes   Thread Pool Worker
             Coroutine             executes function

══════════════════════════════════════════════════════════════════════

              ASYNC FUNCTION EXECUTION

async def get_posts():

        │
        ▼
Python creates Coroutine Object
        │
        ├── Local variables
        ├── Current execution line
        ├── Function state
        └── Dependency objects (AsyncSession, etc.)
        │
        ▼
Event Loop starts executing coroutine
        │
        ▼
await db.execute(...)
        │
        ▼
Coroutine is PAUSED
(State is preserved)
        │
        ▼
Event Loop checks:
"Is another coroutine ready to run?"
        │
   ┌────┴────┐
   │         │
  Yes        No
   │         │
   ▼         ▼
Run next   Wait for an event
Coroutine  (DB response/new request)
   │
   ▼
Database completes operation
        │
        ▼
Event Loop resumes paused coroutine
        │
        ▼
Execution continues after await
        │
        ▼
Return Response
        │
        ▼
FastAPI → Uvicorn → Client
```
