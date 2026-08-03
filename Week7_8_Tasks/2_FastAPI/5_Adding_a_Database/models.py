from __future__ import annotations
# Allows us to reference classes before they are defined (Forward References)

from datetime import UTC, datetime

# SQLAlchemy column types
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text

# ORM helpers
# Mapped -> Type hint for ORM attributes
# mapped_column -> Defines a database column
# relationship -> Defines relationships between tables
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Base class that all models inherit from
from database import Base


# ---------------- USER TABLE ----------------
class User(Base):
    # User → Python class (ORM model)
    # Base → Makes SQLAlchemy recognize this class as a database table.

    # Database table name
    __tablename__ = "users"

    # Primary Key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # Username (must be unique)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # Email (must be unique)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # Stores profile image filename
    # None means user hasn't uploaded an image
    image_file: Mapped[str | None] = mapped_column(String(200), nullable=True, default=None )

    # One User → Many Posts
    # This does NOT create a database column.
    # It lets us access all posts written by a user.
    posts: Mapped[list[Post]] = relationship(
        back_populates="author"
    )

    # Returns profile image URL
    # If no image exists, returns default image
    @property
    def image_path(self) -> str:
        if self.image_file:
            return f"/media/profile_pics/{self.image_file}"
        return "/static/profile_pics/default.jpg"


# ---------------- POST TABLE ----------------
class Post(Base):

    # Database table name
    __tablename__ = "posts"

    # Primary Key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # Post title
    title: Mapped[str] = mapped_column(String(100),nullable=False)

    # Post content
    content: Mapped[str] = mapped_column(Text,nullable=False )

    # Foreign Key
    # Links each post to one user
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # Automatically stores current UTC time
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    # Many Posts → One User
    # Gives access to the user who wrote this post.
    # Example:
    # post.author
    author: Mapped[User] = relationship(
        back_populates="posts"
    )