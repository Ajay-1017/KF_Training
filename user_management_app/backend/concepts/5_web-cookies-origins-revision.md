# Revision Notes — Cookies, SameSite, Origins, Hosts & Ports

## 1. Cookie Security Settings

### HttpOnly

- JavaScript cannot read/access the cookie.
- Browser can still automatically send the cookie with HTTP requests.
- Useful for sensitive cookies such as access and refresh tokens.

**Remember:** `HttpOnly → JavaScript cannot read the cookie`

### Secure

- Cookie is sent only over **HTTPS**.
- Protects the cookie from travelling over normal HTTP.
- In local development using `http://127.0.0.1`, `secure=True` may prevent the cookie from being sent.

**Remember:** `Secure → Cookie only travels over HTTPS`

### SameSite

- Controls whether the browser sends a cookie in **cross-site contexts**.
- Helps protect against unwanted cross-site requests such as CSRF.

Common values:

- `Strict` → very restrictive; cookie is limited to same-site contexts.
- `Lax` → balanced; blocks most cross-site cookie requests but allows certain safe top-level navigations.
- `None` → allows cross-site cookies; requires `Secure=True`.

**Remember:** `SameSite → Controls cross-site cookie sending`

---

## 2. What Does `SameSite="lax"` Mean?

Imagine you are logged into `bank.com`.

The browser stores:

```text
access_token = ABC123
```

If another website tries to make a background request to `bank.com`, `SameSite=Lax` generally prevents the browser from attaching the bank cookie.

```text
evil.com
   ↓
background request
   ↓
bank.com
   ↓
cookie ❌
```

But if you click a normal link that navigates you to `bank.com`, the cookie may be sent.

```text
other-site
   ↓
user clicks link
   ↓
bank.com
   ↓
cookie may be sent ✅
```

### Main idea

> `SameSite=Lax` means: don't normally send my cookie with cross-site requests, but allow certain safe top-level navigations.

---

## 3. Origin

An **origin** is:

```text
Origin = Scheme + Host + Port
```

Example:

```text
http://127.0.0.1:8000
```

Breakdown:

```text
http       → scheme
127.0.0.1  → host
8000       → port
```

Two URLs have the **same origin** only when scheme, host, and port all match.

### Example

```text
http://example.com:8000
http://example.com:8000
```

Same origin ✅

But:

```text
http://example.com:8000
http://example.com:9000
```

Different origin ❌ because the ports are different.

Also:

```text
http://example.com:8000
https://example.com:8000
```

Different origin ❌ because the schemes are different.

---

## 4. Scheme

The scheme tells the browser how to communicate.

Common examples:

```text
http://
https://
```

`https` is the encrypted version using TLS.

```text
http://example.com
https://example.com
```

These are different origins because the scheme is different.

---

## 5. Host

The host identifies the machine/server being contacted.

Examples:

```text
google.com
api.example.com
127.0.0.1
localhost
```

A domain name such as `myapp.com` can resolve through DNS to an IP address.

Conceptually:

```text
Browser
   ↓
myapp.com
   ↓
DNS
   ↓
Server IP address
```

---

## 6. Port

A port identifies a particular service/application on a machine.

Think of the computer as a building and ports as different doors.

```text
Your computer
127.0.0.1
│
├── :5500 → Frontend
├── :8000 → FastAPI
└── :5432 → PostgreSQL
```

So:

```text
http://127.0.0.1:5500
```

means roughly:

> Talk to the application running on port `5500` on this computer.

And:

```text
http://127.0.0.1:8000
```

means:

> Talk to the application running on port `8000` on this computer.

---

## 7. `127.0.0.1`

`127.0.0.1` is the **loopback address**.

It means:

> **This computer itself.**

Every laptop can have `127.0.0.1`, but it points to that particular laptop.

Example:

```text
Laptop A
127.0.0.1 → Laptop A itself

Laptop B
127.0.0.1 → Laptop B itself
```

Think of `127.0.0.1` as the word **"me"**.

For different people, "me" refers to different people.

Similarly, `127.0.0.1` refers to the computer that is using it.

---

## 8. How Two Computers Communicate

`127.0.0.1` points back to the current computer, so it is not normally used to reach another laptop.

Example:

```text
Laptop A
192.168.1.10

Laptop B
192.168.1.20
```

Laptop A can communicate with Laptop B using:

```text
192.168.1.20
```

instead of:

```text
127.0.0.1
```

### Remember

```text
127.0.0.1 → this computer
192.168.x.x → another device on the local network (commonly)
```

---

## 9. Your FastAPI Project

Your current development setup is:

```text
Frontend
http://127.0.0.1:5500

Backend
http://127.0.0.1:8000
```

They have:

```text
Frontend:
scheme → http
host   → 127.0.0.1
port   → 5500

Backend:
scheme → http
host   → 127.0.0.1
port   → 8000
```

Therefore:

```text
Different port
      ↓
Different origin
```

But they are still using the same host/site context for the local example.

---

## 10. Origin vs Site

This is the key distinction.

### Origin

Cares about:

```text
scheme + host + port
```

Your frontend and backend:

```text
127.0.0.1:5500
127.0.0.1:8000
```

are **different origins** because their ports differ.

### Site

For the common cookie discussion, the site relationship is broader and does **not** treat a different port by itself as a different site.

So:

```text
127.0.0.1:5500
127.0.0.1:8000
```

can be:

```text
Different origins
        +
Same-site context
```

---

## 11. CORS vs SameSite

These solve different problems.

### CORS

Asks:

> **"Is this different origin allowed to communicate with my API?"**

Your project:

```text
Frontend
127.0.0.1:5500
      ↓
      ↓ request
      ↓
Backend
127.0.0.1:8000
```

Because the origins differ, CORS rules apply.

Your FastAPI configuration allows the frontend origin:

```python
allow_origins=["http://127.0.0.1:5500"]
allow_credentials=True
```

### SameSite

Asks:

> **"Should this cookie be sent in this site context?"**

So:

```text
CORS
 ↓
origin relationship

SameSite
 ↓
cookie/site relationship
```

### Important

```text
Different origin ≠ automatically different site
```

A different **port** makes origins different, but does not by itself make sites different.

---

## 12. Easy Mental Model

Think of a computer as a building.

```text
Host = building
Port = door/service
Scheme = communication method
Origin = exact combination of all three
```

Example:

```text
https://myapp.com:8000
```

means:

```text
https   → how
myapp.com → where
8000    → which service
```

---

## 13. Final Quick Revision

```text
Cookie
│
├── HttpOnly → JavaScript cannot read it
│
├── Secure   → only send over HTTPS
│
└── SameSite → controls cross-site cookie sending
```

```text
URL
│
├── Scheme → http / https
├── Host   → example.com / 127.0.0.1
├── Port   → 5500 / 8000
└── Path   → /users/me
```

```text
Origin = Scheme + Host + Port
```

```text
127.0.0.1 = "this computer"
```

```text
Different port
    ↓
Different origin
```

```text
CORS
→ controls cross-origin communication

SameSite
→ controls cookie behavior across sites
```
