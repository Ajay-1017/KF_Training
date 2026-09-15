from sqlalchemy.ext.asyncio import AsyncSession , async_sessionmaker , create_async_engine
from sqlalchemy.orm import DeclarativeBase

database_url = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(
    database_url,
    connect_args={"check_same_thread": False}
)

AsyncSessionLocal = async_sessionmaker(
    engine ,
    class_ = AsyncSession,
    expire_on_commit=False
    # expire_on_commit=True → "After saving, forget what you know. Reload from the database the next time someone asks."
    # expire_on_commit=False → "After saving, keep the values you already have in memory. Don't reload unless I explicitly ask."
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session






