from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import Integer , String, Boolean, ForeignKey , DateTime
from sqlalchemy.orm import Mapped , mapped_column , relationship

from database import Base


class User(Base): 

    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer, primary_key = True)

    public_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    
    email : Mapped[str] = mapped_column(String(50), unique = True, nullable=False)

    hash_password : Mapped[str] = mapped_column(String(100), nullable = False)

    is_active : Mapped[bool] = mapped_column(Boolean,nullable = False,default=True)

    user_info : Mapped[UserInfo] = relationship(
        back_populates="user", 
        cascade="all, delete-orphan"
    )

    sessions: Mapped[list[Session]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )   

class UserInfo(Base):

    __tablename__ = "user_info"

    id : Mapped[int] = mapped_column(Integer,primary_key=True)

    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id",ondelete="CASCADE"),
        unique = True,
        nullable = False,
    )

    full_name : Mapped[str] = mapped_column(String(50), nullable=False)

    phone : Mapped[str]	= mapped_column(String(10), unique=True, nullable=False)

    role : Mapped[str] = mapped_column(String(25), nullable=False)

    user : Mapped[User] = relationship(
        back_populates="user_info"
    )


class Session(Base):

    __tablename__ = "sessions"

    id : Mapped[int] = mapped_column(Integer,primary_key=True)

    session_id: Mapped[str] = mapped_column(String(36),unique=True,nullable=False)

    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False
        )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    refresh_token_hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    
    user: Mapped[User] = relationship(
        back_populates="sessions"
    )
