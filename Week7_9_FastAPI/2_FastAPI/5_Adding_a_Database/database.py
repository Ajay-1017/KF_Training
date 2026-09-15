# create_engine -> Creates the Engine (the bridge to the database)
# It does NOT immediately open a database connection.
from sqlalchemy import create_engine

# DeclarativeBase -> Base class that all ORM models inherit from.
# sessionmaker -> Factory used to create Session objects.
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# sqlite:/// = SQLite database
# ./ = current project folder
# blog.db = database file

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    # SQLite normally allows a connection to be used only
    # in the thread where it was created.
    # FastAPI may handle requests using different threads,
    # so we disable this restriction.
)

# Session factory
# Every call to SessionLocal() creates a new database session.

# FLOW :

        # SQLite Database
        #         ▲
        #         │
        #         │
        #     Engine
        #         ▲
        #         │ bind=engine
        #         │
        # Session Factory (sessionLocal)
        #         ▲
        #         │ sessionLocal()
        #         │
        #      Session (db)
        #         ▲
        #         │
        # db.execute(...)
        # db.commit(...)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, # "quickly send pending changes to the database" is called flush.
    bind=engine
)

# Explanation :

        # db.add(user)
        #         │
        #         ▼
        # Session remembers object

        # db.flush()
        #         │
        #         ▼
        # Database receives SQL
        # (BUT transaction is still open)

        # db.commit()
        #         │
        #         ▼
        # Database permanently saves changes

# Base class for all ORM models (tables)
# Any class that inherits from me should be treated as a database table (ORM model)
class Base(DeclarativeBase):
    pass

# Dependency
# Creates a session for each request and closes it automatically.
def get_db():

# FLOW :
        #   get_db()
        #      │
        # Open Session
        #      │
        #      ▼
        # yield db
        #      │
        #      │   ← Function is sleeping
        #      │
        #      ├──────────────► FastAPI runs endpoint
        #      │                  db.execute()
        #      │                  db.commit()
        #      │                  return response
        #      │
        #      ▼
        # Wake up
        #      │
        # Exit with block
        #      │
        # Close Session
    with SessionLocal() as db:
        yield db

# Complete FLOW :

        # Application Starts
        #         │
        #         ▼
        # Read Database URL
        #         │
        #         ▼
        # Create Engine
        #         │
        #         ▼
        # Create Session Factory (SessionLocal)
        #         │
        #         ▼
        # Define Base Class
        #         │
        #         ▼
        # User Sends Request
        #         │
        #         ▼
        # get_db() dependency runs
        #         │
        #         ▼
        # SessionLocal() creates a Session
        #         │
        #         ▼
        # Session uses Engine to communicate with DB
        #         │
        #         ▼
        # Endpoint performs CRUD operations
        #         │
        #         ▼
        # Request finishes
        #         │
        #         ▼
        # Session closes automatically