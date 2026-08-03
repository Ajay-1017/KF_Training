from fastapi import FastAPI,Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException 



app = FastAPI()
app.mount ("/static" , StaticFiles(directory = "static") , name = "static")

templates = Jinja2Templates(directory= "templates")

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

@app.get("/posts",include_in_schema = False)
@app.get("/",include_in_schema=False)
def home(request : Request):
    return templates.TemplateResponse(request,"home.html",{"title" : "home" , "posts" : posts })


@app.get("/posts/{post_id}",include_in_schema=False)
def post_page( post_id : int , request : Request):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post" : post , "title" : title}
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "post not found")


@app.get("/api/posts/")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_posts(post_id : int): # by default path parameters are string 
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "post not found")


# StarletteHTTPException Handler
@app.exception_handler(StarletteHTTPException) 
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message}
        )
    
    return templates.TemplateResponse(
        request,
        "error.html", {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code = exception.status_code
    )



# 1. StarletteHTTPException Flow

# Case 1: Invalid Endpoint

        # Example:
        # GET /api/postsss

# Client (Browser/API)
#         │
#         ▼
#      Uvicorn
#         │
#         ▼
#      FastAPI
#         │
#         ▼
# Searches for matching endpoint
#         │
#         ▼
# Endpoint NOT found
#         │
#         ▼
# Starlette automatically raises

# StarletteHTTPException(
#     status_code=404,
#     detail="Not Found"
# )

#         │
#         ▼
# general_http_exception_handler()
#         │
#         ▼
# Checks request path

# if "/api"
#       │
#       ├────────► JSONResponse
#       │
#       └────────► HTML error page




# Case 2: Manually Raised HTTPException

# Example :

# @app.get("/api/posts/{post_id}")
# def get_post(post_id: int):

#     for post in posts:
#         if post["id"] == post_id:
#             return post

#     raise HTTPException(
#         status_code=404,
#         detail="Post not found"
#     )

# Client
#       │
#       ▼
# FastAPI finds endpoint
#       │
#       ▼
# Runs get_post()
#       │
#       ▼
# Post not found
#       │
#       ▼
# raise HTTPException(
#     status_code=404,
#     detail="Post not found"
# )
#       │
#       ▼
# FastAPI passes exception
# to Starlette exception handler
#       │
#       ▼
# general_http_exception_handler(
#     request,
#     exception
# )
#       │
#       ▼
# exception.status_code = 404
# exception.detail = "Post not found"
#       │
#       ▼
# message = exception.detail
#       │
#       ▼
# If request starts with "/api"

# ↓

# Return

# {
#     "detail":"Post not found"
# }

# Else

# ↓

# Render error.html




# RequestValidationError Handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )

# 2. RequestValidationError Flow

# case : Invalid Request

# Example :
# GET /api/posts/abc

# Client
#       │
#       ▼
# FastAPI receives request
#       │
#       ▼
# Checks parameter

# post_id : int
#       │
#       ▼
# Received

# abc
#       │
#       ▼
# Cannot convert abc to integer
#       │
#       ▼
# FastAPI raises

# RequestValidationError
#       │
#       ▼
# validation_exception_handler()
#       │
#       ▼
# Checks request path

# /api ?

# Yes

# ↓

# JSONResponse

# No

# ↓

# error.html