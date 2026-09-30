# CORS:
# "Is this browser origin/method allowed by CORS?"

# Custom middleware:
# "Does our application accept this request method?"

# Authentication:
# "Is the user authenticated?"

# Authorization:
# "Can this user perform this operation?"

from typing import Annotated
from datetime import timedelta
from config import settings
from datetime import UTC , datetime
import time
import uuid

from fastapi import (
    FastAPI, 
    HTTPException, 
    status, 
    Response, 
    Request,
    Depends,
    Cookie
    )
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select , func
from sqlalchemy.orm import Session
from schema import  UserCreate , UserResponse , UserUpdate , LoginForm


from auth import (
    hash_password , 
    verify_password ,
    create_access_token, 
    verify_access_token,
    create_refresh_token,
    verify_refresh_token,
    hash_refresh_token,
    ensure_utc,
    CurrentUser,
    AdminUser
)

from database import engine , Base , get_db
import models as models

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()
Base.metadata.create_all(bind = engine)

#-------------- MiddleWare--------------#

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def user_management_middleware(request : Request , call_next):

    # method validation 
    allowed_methods = {"GET","POST","PATCH","DELETE","OPTIONS"}

    if request.method not in  allowed_methods:

        # log warning
        logger.warning(
        "%s %s -> 405 HTTP method not allowed",
        request.method,
        request.url.path
    )
        return JSONResponse(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            content={"detail" :"HTTP method not allowed"}
        )

    start_time = time.perf_counter()
    exception  = None

    try:
        response = await call_next(request)

    except Exception as e:
        exception = e
        raise
    
    finally:
        end_time = time.perf_counter()
        elaspsed_time = end_time - start_time

    if exception is None:
        # log info
        logger.info("%s %s -> %s | %.4fs",
                request.method,
                request.url.path,
                response.status_code,
                elaspsed_time
            )

    else:
        # log error 
        logger.error("something went wrong -> %s | %s",
                    exception,
                    elaspsed_time)

    return response


#------------------API Endpoints------------------#

@app.get("/") # public access
def home():
    return {"message" :"user_management_app"}

@app.post("/users" , response_model=UserResponse , status_code=status.HTTP_201_CREATED)
def create_user(admin_user : AdminUser , create_user : UserCreate, db:Annotated[Session ,Depends(get_db)]):
    
    result = db.execute(
        select(models.User)
        .where(func.lower(models.User.email) == create_user.email.lower())
    )

    already_exist_email = result.scalars().first()

    if already_exist_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = "email_id is already exist"
        )
    
    result = db.execute(
        select(models.UserInfo)
        .where(models.UserInfo.phone == create_user.user_info.phone)
    )

    already_exist_phone = result.scalars().first()

    if already_exist_phone:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="phone number is already exist"
        )
    
    try:
        user = models.User(
            email = create_user.email,
            hash_password = hash_password(create_user.password),
            is_active = create_user.is_active 
        )

        db.add(user)
        db.flush()

        created_user_info = models.UserInfo(
            user_id = user.id,
            full_name = create_user.user_info.full_name,
            phone = create_user.user_info.phone,
            role = create_user.user_info.role.value
        )

        db.add(created_user_info)
        db.commit()

        db.refresh(user)
        db.refresh(created_user_info)

        return user

    except Exception:
        db.rollback()
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Failed to create user"
    )


@app.post("/users/token") # public access
def login_for_access_token(
    form_data: Annotated[LoginForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
    response : Response
):

    result = db.execute(
        select(models.User)
        .where(func.lower(models.User.email) == form_data.username.lower()),
    )

    user = result.scalars().first()

    if not user or not verify_password(form_data.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is inactive",
        )

    # create session
    session_id = str(uuid.uuid4())
    refresh_token_jti = str(uuid.uuid4())

    session = models.Session(
        session_id=session_id,
        user_id=user.id,
        expires_at=datetime.now(UTC) + timedelta(
            days=settings.refresh_token_expire_days
        )
    )

    db.add(session)

    # create access token
    access_token_expires = timedelta(minutes = settings.access_token_expire_minutes)

    access_token = create_access_token(
        data={
            "sub": user.public_id,
            "sid" : session_id
            },
        expires_delta=access_token_expires,
    )

    refresh_token = create_refresh_token(
        data={
            "sub": user.public_id,
            "sid": session_id,
            "jti" : refresh_token_jti
            }
    )

    session.refresh_token_hash = hash_refresh_token(refresh_token)

    db.commit()

    response.set_cookie(
        key="access_token",
        value = access_token,
        httponly=True,
        samesite = "lax"
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="lax",
        max_age = settings.refresh_token_expire_days * 24 * 60 * 60
    )   

    return {
    "message": "Login successful",
    "publicId": user.public_id
    }




@app.get("/users", response_model=list[UserResponse])
def get_users( admin_user: AdminUser, db : Annotated[Session,Depends(get_db)]):

    result = db.execute(
        select(models.User)
    )
    users = result.scalars().all()

    return users


@app.get("/users/{public_id}", response_model=UserResponse)
def get_user(public_id : str , current_user : CurrentUser , db : Annotated[Session,Depends(get_db)]):

    result = db.execute(
        select(models.User).where(models.User.public_id == public_id )
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "user not found"
        )
    
    if current_user.user.user_info.role != "admin":
        if public_id != current_user.user.public_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail = "not allowed to access this user"
            )
        return current_user.user

    return user




@app.patch("/users/{public_id}", response_model=UserResponse)
def update_user_profile(public_id : str , update_user : UserUpdate , current_user : CurrentUser , db : Annotated[Session,Depends(get_db)]):
    
    result = db.execute(
        select(models.User).where(models.User.public_id == public_id )
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "user not found"
        ) 
    
    if update_user.email is not None:
        result = db.execute(
            select(models.User)
            .where(
                func.lower(models.User.email) == update_user.email.lower(),
                models.User.public_id != public_id
            )
        )

        already_exist_email = result.scalars().first()

        if already_exist_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail = "email_id is already exist"
            )
    
    if update_user.user_info is not None and update_user.user_info.phone is not None:

        result = db.execute(
            select(models.UserInfo)
            .where(
                models.UserInfo.phone == update_user.user_info.phone,
                models.UserInfo.user_id != user.id
            )
        )

        already_exist_phone = result.scalars().first()

        if already_exist_phone:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="phone number is already exist"
            )

    if public_id == current_user.user.public_id or current_user.user.user_info.role == "admin":

        try:
            updated_data = update_user.model_dump(exclude_unset = True)

            for field, value in updated_data.items():

                if field == "is_active" and current_user.user.user_info.role != "admin":
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail = "needs admin access to change this"
                    )
                
                elif field == "password":
                    user.hash_password = hash_password(value)

                elif field == "user_info":

                    for info_field, info_value in value.items():
                        if info_field == "role" and current_user.user.user_info.role != "admin":
                            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="needs admin access to change role"
                            )
                        
                        setattr(user.user_info, info_field, info_value)

                else:
                    setattr(user, field, value)

            db.commit()
        
        except HTTPException:
            db.rollback()
            raise

        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update user"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="not allowed to update this user"
        )

    db.refresh(user)

    return user  


@app.delete("/users/{public_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
            public_id : str,
            db : Annotated[Session ,Depends(get_db)],
            admin_user : AdminUser
        ):

    result = db.execute(
        select(models.User)
        .where(models.User.public_id == public_id)
    )

    user  = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "user not found"
        )

    if user.public_id == admin_user.public_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = "not allowed to delete the own admin profile itself"
        )

    db.delete(user)
    db.commit()



@app.post("/users/refresh")
def refresh_access_token(
    refresh_token: Annotated[str | None, Cookie(alias="refresh_token")],
    response: Response,
    db: Annotated[Session, Depends(get_db)],
):
    
    if refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token is missing",
        )
    token_data = verify_refresh_token(refresh_token)

    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    public_id, session_id , jti = token_data

    result = db.execute(
        select(models.User).where(models.User.public_id == public_id)
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is inactive",
        )
    
    session_result = db.execute(
    select(models.Session).where(
        models.Session.session_id == session_id
        )
    )

    session = session_result.scalars().first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session not found",
        )
    if session.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session",
        )

    if ensure_utc(session.expires_at) <= datetime.now(UTC):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired",
        )
    
    if session.revoked_at is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session revoked",
        )
    
    presented_token_hash = hash_refresh_token(refresh_token)

    if session.refresh_token_hash != presented_token_hash:

        session.revoked_at = datetime.now(UTC)
        db.commit()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    new_refresh_token_jti = str(uuid.uuid4())

    new_refresh_token = create_refresh_token(
    data={
        "sub": public_id,
        "sid": session_id,
        "jti": new_refresh_token_jti,
        }
    )
    session.refresh_token_hash = hash_refresh_token(new_refresh_token)

    access_token = create_access_token(
        data={"sub": user.public_id,
              "sid": session_id,
              }
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite = "lax"
    )
    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        samesite="lax",
        max_age=settings.refresh_token_expire_days * 24 * 60 * 60,
    )

    db.commit()

    return {"message": "Access token refreshed"}


@app.post("/logout")
def logout(
    access_token: Annotated[str | None, Cookie(alias="access_token")],
    response: Response,
    db: Annotated[Session, Depends(get_db)],
):

    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    token_data = verify_access_token(access_token)

    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    public_id, session_id = token_data

    result = db.execute(
    select(models.Session).where(
        models.Session.session_id == session_id
        )
    )
    session = result.scalars().first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session not found"
        )
    session.revoked_at = datetime.now(UTC)
    db.commit()

    response.delete_cookie("access_token",path="/")
    response.delete_cookie("refresh_token",path="/")
    return {"message": "Logout successful"} 

