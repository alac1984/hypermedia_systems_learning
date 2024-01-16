import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from db.async_db import create_engine


@pytest_asyncio.fixture(scope="function")
async def session() -> AsyncSession:
    engine = create_engine(
        "postgresql+asyncpg://postgres:testpassword@localhost:5433/postgres"
    )
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as test_session:
        yield test_session
