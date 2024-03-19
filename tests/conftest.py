from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import delete

from db.async_db import create_engine
from models.contact import Contact


@pytest_asyncio.fixture(scope="function")
async def test_engine():
    engine = create_engine(
        "postgresql+asyncpg://postgres:testpassword@localhost:5433/postgres"
    )

    return engine


@pytest_asyncio.fixture(scope="function")
async def test_session(test_engine) -> AsyncGenerator:
    session_factory = sessionmaker(
        bind=test_engine, class_=AsyncSession, expire_on_commit=False
    )

    session = session_factory()

    try:
        # Set up test data
        contact1 = Contact(
            first_name="Emily",
            last_name="Smith",
            email="emilysmith@gmail.com",
            gender="Female",
            ip_address="192.168.1.10",
            phone_number="5585992112233",
        )

        contact2 = Contact(
            first_name="Carlos",
            last_name="Gomez",
            email="carlosgomez@gmail.com",
            gender="Male",
            ip_address="192.168.2.15",
            phone_number="5585998776655",
        )

        session.add_all([contact1, contact2])
        await session.commit()
        yield session
    finally:
        stmt1 = delete(Contact)  # type: ignore
        await session.execute(stmt1)
        await session.commit()
        await session.close()
