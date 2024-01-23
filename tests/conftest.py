import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import delete

from db.async_db import create_engine
from models.contact import Contact


@pytest_asyncio.fixture(scope="function")
async def session() -> AsyncSession:
    engine = create_engine(
        "postgresql+asyncpg://postgres:testpassword@localhost:5433/postgres"
    )
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as test_session:
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

        test_session.add_all([contact1, contact2])
        await test_session.commit()
        yield test_session
        statement = delete(Contact)
        await test_session.execute(statement)
        await test_session.commit()
        await test_session.close()
