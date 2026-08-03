
# Flow to understand how async works ?
       
            # Application starts
            #        │
            #        ▼
            # uvicorn main:app
            #        │
            #        ▼
            # Creates ONE Event Loop
            #        │
            #        ▼
            # Event Loop keeps running forever
            #        │
            #        ▼
            # ────────────────────────────────────────────

            # Client sends HTTP request
            #        │
            #        ▼
            # FastAPI matches the route
            #        │
            #        ▼
            # Is the endpoint async def?

            #       Yes                            No
            #        │                              │
            #        ▼                              ▼
            # Call async function             Call normal function
            # (get_posts())                   (get_posts())
            #        │                              │
            #        ▼                              ▼
            # Creates a Coroutine Object      Executes immediately
            #        │                              │
            #        ▼                              ▼
            # Give coroutine to Event Loop    Runs until return
            #        │
            #        ▼
            # Event Loop starts executing coroutine
            #        │
            #        ▼
            # Hits await?

            #       Yes                              No
            #        │                                │
            #        ▼                                ▼
            # Pause ONLY this coroutine         Continue until return
            # Save its execution state
            # (current line, local variables, etc.)
            #        │
            #        ▼
            # Is another coroutine ready?

            #       Yes                              No
            #        │                                │
            #        ▼                                ▼
            # Run that coroutine                Event Loop stays idle
            #                                   waiting for an event
            #        │
            #        ▼
            # Database / I/O operation finishes
            #        │
            #        ▼
            # Event Loop marks coroutine as ready
            #        │
            #        ▼
            # Resume EXACTLY after await
            #        │
            #        ▼
            # Continue execution
            #        │
            #        ▼
            # Return response to client


from typing import Annotated
from contextlib import asynccontextmanager

from fastapi.exception_handlers import (
    http_exception_handler , 
    request_validation_exception_handler
)

from fastapi import FastAPI,Request, HTTPException, status, Depends
# Depends -> Dependency injection (inject the database session into our routes) 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException 

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


import models
from database import Base , engine , get_db
from schemas import PostCreate , PostResponse , PostUpdate, UserCreate , UserResponse  , UserUpdate

# create the database tables
@asynccontextmanager
async def lifespan(_app : FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    # Shutdown
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

# Flow

#              FastAPI Starts
#                     │
#                     ▼
#       Calls lifespan(_app)
#                     │
#                     ▼
#       async with engine.begin()
#                     │
#                     ▼
#         Open DB Connection
#                     │
#                     ▼
#  run_sync(Base.metadata.create_all)
#                     │
#                     ▼
#       Create Missing Tables
#                     │
#                     ▼
#                 yield
#                     │
#         (Server handles all requests)
#                     │
#                     ▼
#           Server Shutdown
#                     │
#                     ▼
#      await engine.dispose()
#                     │
#                     ▼
#     Close Connection Pool & Cleanup
#                     │
#                     ▼
#               Application Ends



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
async def home(request: Request, db: Annotated[AsyncSession, Depends(get_db)]):
    # FastAPI, before calling this function, call get_db(), get the Session object it yields, 
    # and pass that Session into the variable db
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        )
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
async def post_page(request: Request, post_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.id == post_id)
        )
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
async def user_posts_page(
    request: Request,
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(
        select(models.User)
        .where(models.User.id == user_id)
        )
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.user_id == user_id)
        )
    posts = result.scalars().all()
    return templates.TemplateResponse(
        request,
        "user_posts.html",
        {"posts": posts, "user": user, "title": f"{user.username}'s Posts"},
    )


#======================================================================================================
# get (post_page)- api Response 
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# get("/api/posts") -> get all posts (api Response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/posts", response_model=list[PostResponse])
async def get_posts(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        )
    posts = result.scalars().all()
    return posts


#------------------------------------------------------------------------------------------------------
# get("/api/posts/{post_id}") -> get specific post (api Response)
#------------------------------------------------------------------------------------------------------

@app.get("/api/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Post)
        .options(models.Post.author)
        .where(models.Post.id == post_id)
        )
    post = result.scalars().first()
    if post:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

#------------------------------------------------------------------------------------------------------
# get(/api/users/{user_id}/posts) -> get specific user all posts (api response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/users/{user_id}/posts" , response_model = list[PostResponse])
async def get_users_posts( user_id : int , db : Annotated[AsyncSession , Depends(get_db)] ):
    result = await db.execute(
    select(models.User)
    .where(models.User.id == user_id)
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND , 
            detail= "user not found"
            )

    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.user_id == user_id))
    posts = result.scalars().all()
    return posts

#======================================================================================================
# get (user_page)- api Response 
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# get(/api/users/{user_id}) -> get user_page (api response)
#------------------------------------------------------------------------------------------------------
@app.get("/api/users/{user_id}" , response_model = UserResponse)
async def get_users(user_id : int , db : Annotated[AsyncSession , Depends(get_db)] ):
    result = await db.execute(
    select(models.User).where(models.User.id == user_id)
    )
    user = result.scalars().first()

    if user:
        return user
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= "user not found")



#======================================================================================================
# post - api Response 
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# post(/api/users/) -> create user_page (api response)
#------------------------------------------------------------------------------------------------------

@app.post("/api/users", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
#                               -> variable_name : Annotated[type, extra_information]
async def create_user(user : UserCreate, db : Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.User)
        .where(models.User.username == user.username)
        )
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Username already exists"
        )
    
    result = await db.execute(
            select(models.User)
            .where(models.User.email == user.email)
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

    db.add(new_user) # adds the object to the sessions pending list in memory

    await db.commit()
    await db.refresh(new_user)

    return new_user

#------------------------------------------------------------------------------------------------------
# post(/api/posts/) -> create post_page (api response)
#------------------------------------------------------------------------------------------------------
@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_post(post: PostCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.User)
        .where(models.User.id == post.user_id))
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
    await db.commit()
    await db.refresh(new_post ,attribute_names=["author"])
    return new_post

#======================================================================================================
# update - api Response 
#======================================================================================================

#------------------------------------------------------------------------------------------------------
# put(/api/posts/{post_id}) -> update post_page(FULL REPLACEMENT) (api response)
#------------------------------------------------------------------------------------------------------
@app.put("/api/posts/{post_id}",response_model=PostResponse)
async def update_post_full( 
    post_id : int , 
    post_data : PostCreate ,  
    db : Annotated[AsyncSession , Depends(get_db)],
):
    result = await db.execute(
        select(models.Post).where(models.Post.id == post_id)
    )
    post = result.scalars().first()

    if not post:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,detail = "post not found"
        )


    if post_data.user_id != post.user_id:
        result = await db.execute(
            select(models.User)
            .options(models.Post.author)
            .where(models.User.id == post_data.user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

    post.title = post_data.title
    post.content = post_data.content
    post.user_id = post_data.user_id

    await db.commit()
    await db.refresh(post , attribute_names=["author"])

    return post 
#------------------------------------------------------------------------------------------------------
# put(/api/users/{user_id}) -> update user_page(FULL REPLACEMENT) (api response)
#------------------------------------------------------------------------------------------------------

@app.put("/api/users/{user_id}" , response_model=UserResponse) 
async def update_user( user_data : UserCreate , user_id : int , db : Annotated[AsyncSession , Depends(get_db)]):
    result = await db.execute(
        select(models.User).where(models.User.id == user_id)
    ) 

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= " user is not found "
        )

    user.username = user_data.username
    user.email = user_data.email

    await db.commit()
    await db.refresh(user)

    return user
    

#------------------------------------------------------------------------------------------------------
# PATCH(/api/posts/{post_id}) -> update post_page(Partial update) (api response)
#------------------------------------------------------------------------------------------------------
@app.patch("/api/posts/{post_id}",response_model=PostResponse)
async def update_post_partial( 
    post_id : int , 
    post_data : PostUpdate ,  
    db : Annotated[AsyncSession , Depends(get_db)],
):
    result = await db.execute(
        select(models.Post).where(models.Post.id == post_id)
    )
    post = result.scalars().first()

    if not post:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,detail = "post not found"
        )


    # updating data production code method
    update_data = post_data.model_dump(exclude_unset = True)

    for field , value in update_data.items():
        setattr(post , field , value)


    await db.commit()
    await db.refresh(post,attribute_names=["author"])

    return post  

#------------------------------------------------------------------------------------------------------
# patch(/api/users/{user_id}) -> update user_page(Partial update) (api response)
#------------------------------------------------------------------------------------------------------

@app.patch("/api/users/{user_id}",response_model=UserResponse)
async def update_user_partial(
    user_id : int,
    user_update : UserUpdate,
    db : Annotated[AsyncSession,Depends(get_db)]
):
    result = await db.execute(
        select(models.User).where(models.User.id == user_id)
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,detail = "post not found"
        )

    if user_update.username is not None and user_update.username != user.username:

        result = await db.execute(
            select(models.User).where(models.User.username == user_update.username )
        )

        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = "Username already exists"
            )

    
    if user_update.email is not None and user_update.email != user.email:

        result = await db.execute(
            select(models.User)
            .where(models.User.email == user_update.email )
        )

        existing_email = result.scalars().first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = "email already exists"
            )
    # updating data manual way 
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.image_file is not None:
        user.image_file = user_update.image_file

    await db.commit()
    await db.refresh(user)
    return user

        
        

    

    
    


#======================================================================================================
# delete - api Response 
#======================================================================================================


#------------------------------------------------------------------------------------------------------
# delete(/api/posts/{post_id}) -> delete post_page (api response)
#------------------------------------------------------------------------------------------------------
@app.delete("/api/posts/{post_id}" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id : int , db : Annotated[AsyncSession , Depends(get_db)]):
    result = await db.execute(
        select(models.Post).where(models.Post.id == post_id)
    )

    post = result.scalars().first()

    if not post :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= " post not found"
        )

    await db.delete(post)
    await db.commit()


#------------------------------------------------------------------------------------------------------
# delete(/api/user/{user_id}) -> delete user_page with all their posts (api response)
#------------------------------------------------------------------------------------------------------
@app.delete("/api/user/{user_id}" , status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id : int , db : Annotated[AsyncSession , Depends(get_db)]):
    result = await db.execute(
    select(models.User).where(models.User.id == user_id)
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )

    await db.delete(user)
    await db.commit()





#------------------------------------------------------------------------------------------------------
# HttpException handlers
#------------------------------------------------------------------------------------------------------


# StarletteHTTPException Handler
@app.exception_handler(StarletteHTTPException) 
async def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    

    if request.url.path.startswith("/api"):
        return await http_exception_handler(request , exception)
    
    message = (
            exception.detail
            if exception.detail
            else "An error occurred. Please check your request and try again."
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
async def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return await request_validation_exception_handler(request,exception)
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

