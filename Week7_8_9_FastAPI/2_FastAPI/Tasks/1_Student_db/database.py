from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker

database_url =  "sqlite:///./student.db"


engine = create_engine(
        database_url,
        connect_args = {
            "check_same_thread" : False
        }
)

sessionLocal = sessionmaker(
    bind = engine,
    autoflush= False,
    autocommit = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    with sessionLocal() as db:
        yield db

        