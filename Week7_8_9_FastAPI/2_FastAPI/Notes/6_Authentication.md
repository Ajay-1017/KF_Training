# FastAPI Authentication - Revision Notes

---

# Authentication = 2 Phases

```text
                    AUTHENTICATION

        ┌─────────────────────────────┐
        │  Phase 1 : Login            │
        │                             │
        │ Verify Email + Password     │
        │ Create JWT Token            │
        └─────────────────────────────┘
                     │
                     ▼
              Client receives JWT
                     │
                     ▼
        ┌─────────────────────────────┐
        │ Phase 2 : Protected APIs    │
        │                             │
        │ Send JWT Token              │
        │ Verify JWT                  │
        │ Return Current User         │
        └─────────────────────────────┘
```

---

# Overall Authentication Flow

```text
                    REGISTRATION

User
 │
 ▼
POST /users
 │
 ▼
hash_password()
 │
 ▼
Argon2 Hash
 │
 ▼
Database
(password_hash)



                    LOGIN

Email + Password
        │
        ▼
POST /token
        │
        ▼
Find User
        │
        ▼
verify_password()
        │
        ▼
Password Correct?
     │          │
     No         Yes
     │          ▼
401 Unauthorized
               │
               ▼
create_access_token()
               │
               ▼
JWT Token
               │
               ▼
Return Token



             PROTECTED REQUEST

Authorization:
Bearer eyJ...

        │
        ▼
oauth2_scheme
        │
        ▼
Extract Token
        │
        ▼
verify_access_token()
        │
        ▼
jwt.decode()
        │
        ▼
Signature Valid?
Expired?
Secret Correct?
        │
        ▼
Extract user_id
        │
        ▼
Query Database
        │
        ▼
Return Current User
```

---

# Complete Project Authentication Architecture

```text
                config.py
                     │
                     │
     SECRET_KEY
     ALGORITHM
     TOKEN EXPIRY
                     │
                     ▼

                 auth.py
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 hash_password verify_password create_access_token
                                      │
                                      ▼
                            verify_access_token

                     ▲
                     │
                users.py

POST /users
      │
hash_password()

POST /token
      │
verify_password()
      │
create_access_token()

GET /me
      │
oauth2_scheme
      │
verify_access_token()

                     ▲
                     │
                models.py

Stores

password_hash

Never Password

                     ▲
                     │
              schemas.py

Request

UserCreate

↓

Response

Token

↓

UserPrivate
```

---

# Registration Flow

```text
Client

username
email
password

      │
      ▼

POST /api/users

      │
      ▼

UserCreate Schema

      │
      ▼

hash_password()

      │
      ▼

Argon2 Hash

      │
      ▼

User ORM Object

      │
      ▼

Database

id
username
email
password_hash
```

---

# Login Flow

```text
Client

POST /api/users/token

username = ajay@gmail.com
password = hello123

            │
            ▼

OAuth2PasswordRequestForm

            │
            ▼

login_for_access_token()

            │
            ▼

Find User By Email

            │
            ▼

verify_password()

            │
      Password Correct?
       │            │
      No           Yes
       │            ▼
   401 Error   create_access_token()

                     │
                     ▼

              JWT Token

                     │
                     ▼

Return Token
```

---

# JWT Creation Flow

```text
create_access_token()

        │
        ▼

data

{

sub : "5"

}

        │
        ▼

Add Expiry

{

sub : "5"

exp : now + 30 min

}

        │
        ▼

jwt.encode()

        │
        ▼

Uses

SECRET_KEY

ALGORITHM

HS256

        │
        ▼

JWT String

eyJhbGc...
```

---

# JWT Structure

```text
JWT

Header
   │
   ▼
{

alg : HS256

}

        +

Payload

{

sub : 5

exp : ...

}

        +

Signature

Generated using

SECRET_KEY
```

---

# Protected Request Flow

```text
Client

GET /api/users/me

Authorization

Bearer eyJ...

        │
        ▼

FastAPI

        │
        ▼

Depends(oauth2_scheme)

        │
        ▼

Extract Token

eyJ...

        │
        ▼

verify_access_token()

        │
        ▼

jwt.decode()

        │
        ▼

Signature Valid?

Expiry Valid?

Algorithm Valid?

        │
        ▼

Payload

{

sub : 5

}

        │
        ▼

Query Database

        │
        ▼

Current User
```

---

# OAuth2PasswordRequestForm Flow

```text
Browser / Swagger

username
password

        │
        ▼

POST /token

        │
        ▼

Depends()

        │
        ▼

OAuth2PasswordRequestForm

        │
        ▼

Python Object

form_data.username

form_data.password

form_data.scope

...

        │
        ▼

login_for_access_token()
```

---

# OAuth2PasswordBearer Flow

```text
HTTP Request

Authorization

Bearer eyJ....

        │
        ▼

Depends(oauth2_scheme)

        │
        ▼

OAuth2PasswordBearer

        │
        ▼

Read Authorization Header

        │
        ▼

Remove

Bearer

        │
        ▼

Return

Token String

eyJ....
```

---

# Dependency Injection Flow

```text
Client Request

        │
        ▼

FastAPI

        │
        ▼

Inspect Function Parameters

        │
        ▼

Depends() Found?

      │            │
     No           Yes
      │            │
      ▼            ▼

Call Route   Resolve Dependency

                  │
                  ▼

Create Object

                  │
                  ▼

Pass Object To Route

                  │
                  ▼

Execute Route
```

---

# FastAPI + Swagger Architecture

```text
Your FastAPI Code

        │
        ▼

FastAPI

        │

Reads

Routes

Schemas

Dependencies

Security

        │
        ▼

Generates

OpenAPI Specification

        │
        ▼

Swagger UI

(/docs)

        │
        ▼

Interactive API Documentation
```

---

# Swagger Authorization Flow

```text
oauth2_scheme

=

OAuth2PasswordBearer()

          │
          ▼

FastAPI

Adds Security Scheme

To OpenAPI

          │
          ▼

Swagger Reads OpenAPI

          │
          ▼

Shows

Authorize Button
```

---

# Config Loading Flow

```text
config.py

      │
      ▼

Settings()

      │
      ▼

BaseSettings

      │
      ▼

SettingsConfigDict

      │
      ▼

Read .env File

      │
      ▼

Load

SECRET_KEY

ALGORITHM

TOKEN EXPIRY

      │
      ▼

Convert To Python Types

      │
      ▼

settings Object

      │
      ▼

Used Everywhere

settings.secret_key

settings.algorithm

settings.access_token_expire_minutes
```

---

# Password Hashing Flow

```text
Plain Password

hello123

      │
      ▼

hash_password()

      │
      ▼

Argon2 Hash

$argon2id$....

      │
      ▼

Database

password_hash
```

---

# Password Verification Flow

```text
Login Password

hello123

        │
        ▼

verify_password()

        │
        ▼

Hash Again

        │
        ▼

Compare

Database Hash

        │
        ▼

Match?

     │        │
    No       Yes
     │        ▼

401      Login Success
```

---

# Token Verification Flow

```text
JWT Token

eyJ....

      │
      ▼

jwt.decode()

      │
      ▼

Verify

Signature

Secret Key

Expiry

Algorithm

      │
      ▼

Extract Payload

{

sub : 5

}

      │
      ▼

Return User ID
```

---

# One-Line Revision

## Registration

```
Password → Hash → Database
```

## Login

```
Email + Password → Verify → JWT Token
```

## Protected API

```
Bearer Token → Extract → Verify → User ID → Database → Current User
```

---

# Difference Table

| OAuth2PasswordRequestForm   | OAuth2PasswordBearer       |
| --------------------------- | -------------------------- |
| Reads Login Form            | Reads Authorization Header |
| Used During Login           | Used After Login           |
| Returns Form Object         | Returns Token String       |
| Input = username + password | Input = Bearer Token       |
| `/token` Endpoint         | Protected Endpoints        |

---

# FastAPI Authentication Cheat Sheet

```
Client
 │
 ▼
Register
 │
 ▼
Hash Password
 │
 ▼
Database
 │
 ▼
Login
 │
 ▼
Verify Password
 │
 ▼
Create JWT
 │
 ▼
Return JWT
 │
 ▼
Client Stores JWT
 │
 ▼
Authorization: Bearer <JWT>
 │
 ▼
OAuth2PasswordBearer
 │
 ▼
verify_access_token()
 │
 ▼
Database
 │
 ▼
Current User
```
