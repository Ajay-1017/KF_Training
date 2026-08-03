from typing import Annotated

from fastapi import FastAPI,Request, HTTPException, status, Depends
# Depends -> Dependency injection (inject the database session into our routes) 

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from starlette.exceptions import HTTPException as StarletteHTTPException 

from sqlalchemy import select
from sqlalchemy.orm import Session


import models
from database import Base , engine , get_db
from schemas import PostCreate , PostResponse , UserCreate , UserResponse

# create the database tables
Base.metadata.create_all(bind = engine)


app = FastAPI()
app.mount ("/static" , StaticFiles(directory = "static") , name = "static")
app.mount("/media", StaticFiles(directory="media"), name = "media")

templates = Jinja2Templates(directory= "templates")

#======================================================================================================
# Template Response
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# get("/") -> Home_page (template response)
#------------------------------------------------------------------------------------------------------

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request, db: Annotated[Session, Depends(get_db)]):
    # FastAPI, before calling this function, call get_db(), get the Session object it yields, 
    # and pass that Session into the variable db
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    
                    # db.execute()
                    #         │
                    #         ▼
                    #      Result
                    #         │
                    #         ▼
                    #       Row(s)
                    #         │
                    #         ├──────────────┐
                    #         │              │
                    # One value         Multiple values
                    # (User,)           (id, username)
                    #    │                    │
                    #    ▼                    ▼
                    # scalars()           No scalars()
                    #    │
                    #    ▼
                    # User

    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )



#------------------------------------------------------------------------------------------------------
# get("/posts/{post_id}") -> post_page (template response)
#------------------------------------------------------------------------------------------------------
@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if post:
        title = post.title[:50]
        return templates.TemplateResponse(
            request,
            "post.html",
            {"post": post, "title": title},
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


#------------------------------------------------------------------------------------------------------
# get("/users/{user_id}/posts") -> user's post_page (template response)
#------------------------------------------------------------------------------------------------------
@app.get("/users/{user_id}/posts", include_in_schema=False, name="user_posts")
def user_posts_page(
    request: Request,
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = db.execute(select(models.Post).where(models.Post.user_id == user_id))
    posts = result.scalars().all()
    return templates.TemplateResponse(
        request,
        "user_posts.html",
        {"posts": posts, "user": user, "title": f"{user.username}'s Posts"},
    )


#======================================================================================================
# api Response - get
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# get("/api/posts") -> get all posts (api Response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/posts", response_model=list[PostResponse])
def get_posts(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    return posts


#------------------------------------------------------------------------------------------------------
# get("/api/posts/{post_id}") -> get specific post (api Response)
#------------------------------------------------------------------------------------------------------

@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if post:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


#------------------------------------------------------------------------------------------------------
# get(/api/users/{user_id}) -> get user_page (api response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/users/{user_id}" , response_model = UserResponse)
def get_users(user_id : int , db : Annotated[Session , Depends(get_db)] ):
    result = db.execute(
    select(models.User).where(models.User.id == user_id)
    )
    user = result.scalars().first()

    if user:
        return user
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= "user not found")

#------------------------------------------------------------------------------------------------------
# get(/api/users/{user_id}/posts) -> get specific user all posts (api response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/users/{user_id}/posts" , response_model = list[PostResponse])
def get_users_posts( user_id : int , db : Annotated[Session , Depends(get_db)] ):
    result = db.execute(
    select(models.User).where(models.User.id == user_id)
    )

    user = result.scalars.first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND , 
            detail= "user not found"
            )

    result = db.execute(select(models.Post).where(models.Post.user_id == user_id))
    posts = result.scalars().all()
    return posts


#======================================================================================================
# api Response - post
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# post(/api/users/) -> create user_page (api response)
#------------------------------------------------------------------------------------------------------

@app.post("/api/users", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
#                               -> variable_name : Annotated[type, extra_information]
def create_user(user : UserCreate, db : Annotated[Session , Depends(get_db)]):
    result = db.execute(
        select(models.User).where(models.User.username == user.username)
        )
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Username already exists"
        )
    
    result = db.execute(
            select(models.User).where(models.User.email == user.email)
            )
    existing_email = result.scalars().first()
    
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Email already exists"
        )

    new_user = models.User(
        username = user.username,
        email = user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#------------------------------------------------------------------------------------------------------
# post(/api/posts/) -> create user_page (api response)
#------------------------------------------------------------------------------------------------------
@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.User).where(models.User.id == post.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#------------------------------------------------------------------------------------------------------
# HttpException handlers
#------------------------------------------------------------------------------------------------------


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

