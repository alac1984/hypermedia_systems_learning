import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import AppSettings
from db.async_db import create_engine


@pytest_asyncio.fixture(scope="function")
async def session() -> AsyncSession:
    settings = AppSettings()

    engine = create_engine(settings.DATABASE_URL)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as test_session:
        yield test_session

