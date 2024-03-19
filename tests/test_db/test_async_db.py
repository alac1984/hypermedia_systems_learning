import pytest
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from db.async_db import create_engine, get_session
from settings import AppSettings


def test_create_engine():
    settings = AppSettings()  # type: ignore
    engine = create_engine(settings.DATABASE_URL)

    assert isinstance(engine, AsyncEngine)


@pytest.mark.asyncio
async def test_get_session():
    gen = get_session()
    assert isinstance(gen, AsyncGenerator)

    session = await gen.__anext__()
    assert isinstance(session, AsyncSession)
