from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,DeclarativeBase

database_url = "sqlite:///./blog.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    with sessionLocal() as db:
        yield db






