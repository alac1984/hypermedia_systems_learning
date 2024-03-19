from settings import AppSettings
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker


settings = AppSettings()  # type: ignore


def create_engine(url: str) -> AsyncEngine:
    return create_async_engine(url, echo=True, future=True)


engine = create_engine(settings.DATABASE_URL)
session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:  # type: ignore
    session = session_factory()

    try:
        yield session
    finally:
        await session.close()
