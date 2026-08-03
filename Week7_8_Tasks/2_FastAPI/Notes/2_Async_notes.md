# FastAPI Async Programming Notes (Part 1)

# 1. Synchronous vs Asynchronous

### Synchronous (Blocking)

* A request starts executing.
* If it reaches a database query, Python waits until the database responds.
* During this waiting time, that worker cannot continue executing that request.

Example:

```python
posts = db.execute(select(Post))
```

Flow:

```
Request
   │
   ▼
db.execute()
   │
   ▼
Wait for database
   │
   ▼
Continue execution
```

---

### Asynchronous (Non-blocking)

* A request starts executing.
* When it reaches an `await`, the current coroutine pauses.
* The event loop can execute another ready coroutine while waiting.

Example:

```python
posts = await db.execute(select(Post))
```

Flow:

```
Request
   │
   ▼
await db.execute()
   │
   ▼
Pause current coroutine
   │
   ▼
Run another ready coroutine
   │
   ▼
Database finishes
   │
   ▼
Resume paused coroutine
```

---

# 2. Event Loop

The Event Loop is the scheduler that executes asynchronous coroutines.

It is responsible for:

* Running coroutines.
* Pausing them at `await`.
* Resuming them when the awaited operation finishes.

Important:

* The Event Loop starts **once** when Uvicorn starts.
* It does **not** start for every request.

Flow:

```
uvicorn main:app
        │
        ▼
Creates ONE Event Loop
        │
        ▼
Runs forever
```

---

# 3. async def

Example:

```python
async def get_posts():
    ...
```

`async def` **does not execute the function.**

It simply defines a coroutine function.

Think of it as a blueprint.

---

# 4. Coroutine Function vs Coroutine Object

## Coroutine Function

Example:

```python
async def get_posts():
    ...
```

This is only a function definition.

Nothing is running.

---

## Coroutine Object

When FastAPI calls:

```python
get_posts()
```

Python creates a **Coroutine Object**.

The Event Loop executes this coroutine object.

Flow:

```
async def get_posts()
        │
        ▼
Coroutine Function
        │
Call get_posts()
        │
        ▼
Coroutine Object
        │
        ▼
Executed by Event Loop
```

---

# 5. What does await do?

`await` tells the Event Loop:

> "This operation will take time.
> Pause me and execute another ready coroutine."

Example:

```python
result = await db.execute(...)
```

The coroutine pauses.

Only the **current coroutine** pauses.

The Event Loop itself never pauses.

---

# 6. What happens at await?

Suppose:

```python
async def get_posts():
    x = 10
    y = 20

    result = await db.execute(...)

    return result
```

When execution reaches:

```python
await db.execute(...)
```

Python saves the coroutine state.

It stores:

* Current execution line
* Local variables (`x`, `y`)
* Stack frame
* References to objects (for example, `db`)

The coroutine is **paused**, not destroyed.

---

# 7. What happens while a coroutine is paused?

Two possibilities exist.

## Case 1

Another coroutine is ready.

```
Coroutine A
      │
await
      │
Pause
      │
Run Coroutine B
```

---

## Case 2

No other coroutine exists.

```
Coroutine A
      │
await
      │
Pause
      │
Event Loop stays idle
      │
Database finishes
      │
Resume Coroutine A
```

The Event Loop does **not** require another request.

It simply executes other work **if available**.

---

# 8. When does the Event Loop switch?

Very important rule:

The Event Loop switches **only at ****`await`****.**

It does **not** switch:

* because another request arrived
* randomly
* in the middle of normal Python statements

Example:

```python
print(1)
print(2)
print(3)
```

There is no `await`.

The Event Loop cannot interrupt this code.

---

# 9. Correct Request Flow

```
Application starts
       │
       ▼
uvicorn main:app
       │
       ▼
Creates ONE Event Loop
       │
       ▼
Event Loop keeps running forever

──────────────────────────────────

Client Request
       │
       ▼
FastAPI matches route
       │
       ▼
Is endpoint async?

     Yes                 No
      │                   │
      ▼                   ▼
Create Coroutine      Execute normal function
      │
      ▼
Give coroutine to Event Loop
      │
      ▼
Execute coroutine
      │
      ▼
Hits await?

    Yes                 No
     │                   │
     ▼                   ▼
Pause coroutine      Continue execution
Save execution state
     │
     ▼
Another coroutine ready?

    Yes                 No
     │                   │
     ▼                   ▼
Run it            Event Loop waits
     │
     ▼
Database finishes
     │
     ▼
Resume paused coroutine
     │
     ▼
Return response
```

---

# 10. Session vs AsyncSession

## Common misunderstanding

A Session does **not** create threads.

A Session only manages:

* Database connection
* Transaction
* Identity map
* ORM state

---

## Normal Session

Example:

```python
db.execute(...)
```

This is a blocking operation.

The Event Loop cannot pause here because there is no `await`.

---

## AsyncSession

Example:

```python
await db.execute(...)
```

The operation is asynchronous.

The coroutine pauses while waiting for the database.

The Event Loop can execute another coroutine.

---

# 11. One Session Per Request

This is true in both synchronous and asynchronous FastAPI.

Example:

```
Client 1
    │
Session A

Client 2
    │
Session B
```

Each request receives its own session.

This is **independent** of async programming.

---

# 12. Why AsyncSession Exists

The purpose of `AsyncSession` is **not** to create separate sessions.

Separate sessions already exist.

The real purpose is to provide asynchronous database methods.

Comparison:

```
Session

↓

db.execute()

↓

Blocks execution
```

vs

```
AsyncSession

↓

await db.execute()

↓

Coroutine pauses

↓

Event Loop executes another coroutine
```

---

# 13. Mental Model

```
Client Request
      │
      ▼
FastAPI
      │
      ▼
Create Coroutine Object
      │
      ▼
Event Loop executes it
      │
      ▼
await db.execute(...)
      │
      ▼
Coroutine sleeps
      │
      ▼
Event Loop checks for other ready coroutines
      │
      ├── Found one → Execute it
      │
      └── None → Stay idle
      │
      ▼
Database finishes
      │
      ▼
Event Loop resumes the paused coroutine
      │
      ▼
Continue after await
      │
      ▼
Return response
```

# Key Takeaways

* `async def` defines a coroutine function.
* Calling an async function creates a coroutine object.
* The Event Loop executes coroutine objects.
* `await` pauses only the current coroutine.
* The Event Loop switches only at `await`.
* The Event Loop starts once when Uvicorn starts.
* Each request gets its own Session/AsyncSession.
* `AsyncSession` exists because its database operations are awaitable and cooperate with the Event Loop.
