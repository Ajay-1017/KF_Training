# FastAPI + SQLAlchemy Notes

## 1. Dependency Injection

```python
db: Annotated[Session, Depends(get_db)]
```

- `Session` → Type hint (tells Python/IDE what type `db` is).
- `Depends(get_db)` → Tells FastAPI how to create the `db` object.
- FastAPI automatically calls `get_db()` before executing the endpoint.

---

## 2. get_db()

```python
def get_db():
    with SessionLocal() as db:
        yield db
```

### Why `yield` instead of `return`?

- `return` → Ends the function.
- `yield` → Pauses the function.

Flow:

```
Open Session
      ↓
yield db
      ↓
FastAPI executes endpoint
      ↓
Endpoint finishes
      ↓
Resume get_db()
      ↓
Close Session
```

Equivalent concept:

```python
generator = get_db()

db = next(generator)      # yield

endpoint(db)

next(generator)           # resume & close session
```

---

## 3. Session

A `Session` is an object that manages communication with the database.

Common methods:

```python
db.add()
db.execute()
db.commit()
db.rollback()
db.refresh()
db.delete()
db.close()
```

Think of the Session as a **workspace** for one request.

---

## 4. sessionmaker()

```python
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
```

`sessionmaker()` is **not** a Session.

It is a **Session Factory**.

```
Session Factory
      ↓
Session 1
Session 2
Session 3
```

Every request gets a new Session.

---

## 5. bind=engine

```
Database
    ↑
 Engine
    ↑
Session Factory
    ↑
Session
```

`bind=engine` tells every Session which database engine to use.

---

## 6. Why not one global Session?

❌ Bad

```python
db = SessionLocal()
```

All users share the same Session.

Problems:

- Shared transaction
- Data conflicts
- Not thread-safe

✅ Correct

Each request gets its own Session.

---

## 7. autocommit=False

Changes are **not** saved automatically.

You must explicitly call:

```python
db.commit()
```

Advantages:

- Full control
- Supports rollback
- Prevents partial updates

---

## 8. add()

```python
db.add(user)
```

Only places the object inside the Session.

```
Session
✓ User

Database
❌ No row yet
```

---

## 9. flush()

```python
db.flush()
```

Flush sends pending SQL to the database **without committing**.

Example:

```sql
INSERT INTO users ...
```

The row exists only inside the current transaction.

```
Session
        ↓
flush()
        ↓
Database Transaction
        ↓
commit()
        ↓
Permanent Table
```

### Important

Flush:

- ✅ Sends SQL
- ✅ Gets database-generated IDs
- ✅ Makes data available in the current transaction

Flush does **NOT**:

- ❌ Permanently save data
- ❌ Commit the transaction

---

## 10. commit()

```python
db.commit()
```

Commit makes all pending changes permanent.

After commit:

- Data is permanently stored.
- Other database sessions can see it.

---

## 11. rollback()

```python
db.rollback()
```

Removes every uncommitted change.

Useful when an exception occurs.

---

## 12. Crash before commit

```
db.add(user)
db.flush()

💥 Application crashes

No commit()
```

Result:

Database automatically discards the transaction.

The row is **not** saved.

---

## 13. autoflush

When:

```python
autoflush=True
```

Before SQLAlchemy executes a database query, it automatically performs:

```python
db.flush()
```

Example:

```python
db.add(user)

db.execute(select(User))
```

Flow:

```
add(user)
      ↓
Automatic flush
      ↓
SELECT
```

This ensures the query sees the latest changes.

---

## 14. autoflush=False

With:

```python
autoflush=False
```

SQLAlchemy does **not** flush automatically.

Example:

```python
db.add(user)

db.execute(select(User))
```

Since the INSERT was never flushed,

the SELECT cannot find the new user.

You must do:

```python
db.flush()
```

before querying.

---

## 15. Reading Python Object vs Database

Python object:

```python
print(user.username)
```

❌ No flush needed.

Database query:

```python
db.execute(select(User))
```

✅ Requires flush (manual or automatic).

---

## 16. Why flush exists

Main reasons:

- Send pending SQL before queries.
- Get auto-generated IDs.
- Keep the current transaction consistent.

Example:

```python
user = User(username="Ajay")

db.add(user)

db.flush()

print(user.id)
```

Output:

```
1
```

Even though:

```python
db.commit()
```

has not been called yet.

---

# Memory Trick

```
add()
↓
Session Memory

flush()
↓
Database Transaction (Temporary)

commit()
↓
Permanent Database

rollback()
↓
Discard Temporary Changes
```
