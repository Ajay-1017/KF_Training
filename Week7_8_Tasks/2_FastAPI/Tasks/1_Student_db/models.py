from sqlalchemy import Integer , String , DateTime
from sqlalchemy.orm import Mapped , mapped_column , relationship

from Tasks.Student_db.database import Base

from datetime import datetime , UTC

class Student(Base):
    __tablename__ = "student"

    id : Mapped[int] = mapped_column(
        Integer , 
        primary_key=True , 
        index = True
    )


    name : Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    age : Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    email : Mapped[str] = mapped_column(
        String,
        unique = True,
        nullable = False
    )

    department : Mapped[str] = mapped_column(
        String , 
        nullable = False
    )

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        default=lambda: datetime.now(UTC)
    )