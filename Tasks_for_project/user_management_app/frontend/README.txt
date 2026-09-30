SIMPLE USER MANAGEMENT FRONTEND

Folder structure:

frontend_simple/
├── html/
│   ├── login.html
│   └── users.html
├── css/
│   ├── style.css
│   └── users.css
└── js/
    ├── api.js
    ├── login.js
    └── users.js

How to run:

1. Start the FastAPI backend on:
   http://127.0.0.1:8000

2. Serve this frontend with a local HTTP server.
   Example with VS Code:
   - Install Live Server.
   - Open html/login.html with Live Server.

3. Login using an existing backend user.

Important:
- JavaScript never reads the JWT.
- JavaScript never stores the JWT in localStorage/sessionStorage.
- Requests use credentials: "include".
- Backend HttpOnly cookies handle authentication.
- login.js handles login.
- api.js handles common API requests and refresh retry.
- users.js handles the simple dashboard, profile, admin CRUD and logout.

The frontend expects the backend response fields:
publicId
isActive
userInfo
fullName
phone
role

The frontend sends request fields in snake_case:
is_active
user_info
full_name
