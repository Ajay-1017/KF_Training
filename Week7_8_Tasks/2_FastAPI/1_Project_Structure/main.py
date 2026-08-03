# We build a web application using the FastAPI framework.

# Inside that web application, we create API endpoints
# such as GET /, POST /users, etc.

# When a browser (or any client) requests an endpoint:
# 1. Uvicorn receives the HTTP request.
# 2. Uvicorn passes the request to the FastAPI application.
# 3. FastAPI checks which function is registered for that endpoint.
# 4. FastAPI executes that function.
# 5. The function returns a response.
# 6. Uvicorn sends the response back to the client.

from fastapi import FastAPI # "FastAPI" is class from the "fastapi" package
from fastapi.responses import HTMLResponse
app = FastAPI() # Creates a FastAPI application object (our web application).



posts : list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
@app.get("/",response_class=HTMLResponse,include_in_schema=False) 
def home():
    return f"<h1>{posts[1]['title']}</h1>"

@app.get("/api/posts")
def app_posts():
    return posts


