
from datetime import datetime,UTC,timedelta
from typing import Annotated
from dataclasses import dataclass

from fastapi import Depends, HTTPException,status,Cookie

from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
import jwt
import hashlib


from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from database import get_db
import models as models

password_hash = PasswordHash((BcryptHasher(),))

def hash_password(password : str) -> str:
    return password_hash.hash(password) 

def verify_password(plain_password : str , hash_password : str) -> bool:
    return password_hash.verify(plain_password,hash_password)

def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """ Create a JWT access token."""
    to_encode = data.copy()
    to_encode.update({"type":"access"})
    
    if expires_delta:   
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(
            minutes=settings.access_token_expire_minutes,
        )
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        payload = to_encode,
        key = settings.secret_key.get_secret_value(),
        algorithm = settings.algorithm,
    )
    return encoded_jwt



def create_refresh_token(data: dict) -> str:
    """ Create a JWT refresh token."""
    to_encode = data.copy()

    to_encode.update({
        "type": "refresh",
    })


    expire = datetime.now(UTC) + timedelta(
        days=settings.refresh_token_expire_days,
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=settings.secret_key.get_secret_value(),
        algorithm=settings.algorithm,
    )

    return encoded_jwt



def verify_access_token(token: str) -> tuple[str, str] | None:
    """ Verify a JWT access token and return the public ID if valid. """

    try:
        payload = jwt.decode(
            jwt = token,
            key = settings.secret_key.get_secret_value(),
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub","sid"]},
        )

    except jwt.InvalidTokenError:
        return None
    else:
        if payload.get("type") != "access":
            return None
        return payload.get("sub"),payload.get("sid")


    
def verify_refresh_token(token: str) -> tuple[str, str, str] | None:
    """Verify a JWT refresh token and return the public ID if valid."""
    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.secret_key.get_secret_value(),
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub","sid","jti"]}
        )

    except jwt.InvalidTokenError:
        return None
    else:
        if payload.get("type") != "refresh":
            return None

        return (
        payload.get("sub"),
        payload.get("sid"),
        payload.get("jti")
    )



@dataclass
class AuthenticatedUser:
    user: models.User
    session_id: str


def ensure_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)

    return dt.astimezone(UTC)

def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str | None, Cookie(alias="access_token")] = None
):  
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    token_data = verify_access_token(token)

    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    public_id, session_id = token_data

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
    
    return AuthenticatedUser(
        user=user,
        session_id=session_id
    )

CurrentUser = Annotated[AuthenticatedUser, Depends(get_current_user)]



def require_admin(current_user : CurrentUser):

    if current_user.user.user_info.role != "admin":
        raise HTTPException (
            status_code=status.HTTP_403_FORBIDDEN,
            detail = "needs the admin access "
        )

    return current_user.user

AdminUser = Annotated[models.User,Depends(require_admin)]


