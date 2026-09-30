from sqlalchemy import create_engine , event
from sqlalchemy.orm import sessionmaker,DeclarativeBase

# PostgreSQL server
#        │
#        │ localhost:5432
#        │
#        └── Database: user_management
#                     │
#                     ├── users
#                     ├── user_info
#                     └── sessions

from config import settings

engine = create_engine(
    settings.database_url
)

sessionLocal = sessionmaker(
    bind = engine,
    autoflush=False,
    autocommit = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    with sessionLocal() as session:
        yield session

