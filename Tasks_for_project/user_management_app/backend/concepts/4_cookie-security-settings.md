# Cookie Security Settings

## 1. HttpOnly

- JavaScript **cannot read/access** the cookie.
- The browser can still send the cookie with HTTP requests.
- Used to protect sensitive cookies such as `access_token` and `refresh_token`.

**Remember:**
`HttpOnly → JavaScript cannot read the cookie`

---

## 2. Secure

- Cookie is sent only over **HTTPS**.
- Prevents the cookie from travelling over normal unencrypted HTTP.
- Usually used in production.

**Remember:**`Secure → Cookie only travels over HTTPS`

> During local development with `http://127.0.0.1`, `secure=True` may prevent the cookie from being sent.

---

## 3. SameSite

- Controls whether the browser sends the cookie with **cross-site requests**.
- Helps protect against unwanted cross-site requests.

### Common values

| Value      | Meaning                                                   |
| ---------- | --------------------------------------------------------- |
| `strict` | Cookie is restricted to same-site requests                |
| `lax`    | Balanced protection; allows some cross-site situations    |
| `none`   | Allows cross-site cookie sending; requires`Secure=True` |

**Remember:**
`SameSite → Controls cross-site cookie sending`

---

## Quick Revision

```text
HttpOnly → JavaScript cannot read the cookie
Secure   → Cookie only travels over HTTPS
SameSite → Controls cross-site cookie sending
```

## Example

```python
response.set_cookie(
    key="access_token",
    value=access_token,
    httponly=True,
    secure=True,
    samesite="lax"
)
```
