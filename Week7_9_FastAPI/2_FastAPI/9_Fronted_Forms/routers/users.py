## Imports for Users Router
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import PostResponse, UserCreate, UserResponse, UserUpdate

router = APIRouter()

#------------------------------------------------------------------------------------------------------
# post(/api/users/) -> create user_page (api response)
#------------------------------------------------------------------------------------------------------

@router.post("", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
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
# get(/api/users/{user_id}) -> get user_page (api response)
#------------------------------------------------------------------------------------------------------
@router.get("/{user_id}" , response_model = UserResponse)
async def get_users(user_id : int , db : Annotated[AsyncSession , Depends(get_db)] ):
    result = await db.execute(
    select(models.User).where(models.User.id == user_id)
    )
    user = result.scalars().first()

    if user:
        return user
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= "user not found")



#------------------------------------------------------------------------------------------------------
# get(/api/users/{user_id}/posts) -> get specific user all posts (api response)
#------------------------------------------------------------------------------------------------------
@router.get("/{user_id}/posts" , response_model = list[PostResponse])
async def get_users_posts( user_id : int , db : Annotated[AsyncSession , Depends(get_db)] ):
    result = await db.execute(
    select(models.User)
    .where(models.User.id == user_id)
    .order_by(models.Post.date_posted.desc())
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
        .where(models.Post.user_id == user_id)
        .order_by(models.Post.date_posted.desc())
    )
    posts = result.scalars().all()
    return posts

#------------------------------------------------------------------------------------------------------
# put(/api/users/{user_id}) -> update user_page(FULL REPLACEMENT) (api response)
#------------------------------------------------------------------------------------------------------

@router.put("/{user_id}" , response_model=UserResponse) 
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
# patch(/api/users/{user_id}) -> update user_page(Partial update) (api response)
#------------------------------------------------------------------------------------------------------

@router.patch("/{user_id}",response_model=UserResponse)
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


#------------------------------------------------------------------------------------------------------
# delete(/api/user/{user_id}) -> delete user_page with all their posts (api response)
#------------------------------------------------------------------------------------------------------
@router.delete("/{user_id}" , status_code=status.HTTP_204_NO_CONTENT)
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
