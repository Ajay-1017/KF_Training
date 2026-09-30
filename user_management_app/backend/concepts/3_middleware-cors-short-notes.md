# Middleware & CORS — Short Revision Notes

## 1. Middleware

- Middleware sits **between the request and your API endpoint**.
- It can inspect, modify, allow, or reject requests/responses.
- It usually applies to **every request**.

```text
Request
   ↓
Middleware
   ↓
API Endpoint
   ↓
Response
```

---

## 2. Custom Middleware

- Middleware **we write ourselves** for our application's rules.
- Example: checking allowed HTTP methods.

```python
allowed_methods = {
    "GET", "POST", "PATCH", "DELETE", "OPTIONS"
}
```

- If the method isn't allowed → return `405`.

---

## 3. CORS Middleware

**CORS = Cross-Origin Resource Sharing**

- CORS controls **which browser origins can communicate with our backend**.
- It is also a type of middleware.
- FastAPI provides `CORSMiddleware`; we configure it.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

## 4. Important CORS Settings

| Setting | Meaning |
|---|---|
| `allow_origins` | Which websites/origins are allowed |
| `allow_methods` | Which HTTP methods CORS allows |
| `allow_headers` | Which request headers are allowed |
| `allow_credentials` | Allows credentials such as cookies |

---

## 5. `allow_methods=["*"]`

Means:

> **CORS allows all HTTP methods.**

Including:

```text
GET
POST
PATCH
DELETE
OPTIONS
...
```

But this **only applies to CORS middleware**.

---

## 6. CORS vs Custom Middleware

They are separate:

```text
CORS Middleware
↓
"Is this browser origin/request allowed by CORS?"

Custom Middleware
↓
"Does my application's own rule allow this request?"
```

So:

```text
CORS → OPTIONS ✅
Custom middleware → OPTIONS ❌
```

The request can still be rejected.

---

## 7. Why `OPTIONS` Matters

Browsers can send an `OPTIONS` request as a **CORS preflight** before the actual request.

```text
Browser
   ↓
OPTIONS
   ↓
"Can I send this request?"
   ↓
Actual POST/PATCH/etc.
```

Therefore, if our custom middleware checks methods, it should also allow `OPTIONS`.

---

## 8. Middleware ≠ Authentication

Don't confuse them:

```text
CORS
→ Is this browser origin allowed?

Authentication
→ Who is the user?

Authorization
→ What is the user allowed to do?
```

Your project uses `CurrentUser` / `get_current_user()` for authentication.

---

## ⭐ One-Line Memory Trick

> **Middleware = common checkpoint**  
> **CORS = browser-origin checkpoint**  
> **Authentication = Who are you?**  
> **Authorization = What can you do?**
