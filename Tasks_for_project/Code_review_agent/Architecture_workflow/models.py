from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped , mapped_column
from database import Base


class ReviewJob(Base):
    __tablename__ = "review_jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(String, nullable=False)

    source_location: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    review_result: Mapped[str | None] = mapped_column(String, nullable=True)
    attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0)