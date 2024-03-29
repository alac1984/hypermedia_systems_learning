import pytest
from sqlalchemy.sql import text
from sqlmodel import delete

from repository.contact import repo_retrieve_contacts, repo_insert_contact
from models.contact import Contact


@pytest.mark.asyncio
async def test_repo_retrieve_contacts(test_session):
    contacts = await repo_retrieve_contacts(test_session, "Emily")

    assert contacts is not []
    assert len(contacts) == 1


@pytest.mark.asyncio
async def test_repo_insert_contact(test_session):
    contact = Contact(
        first_name="John",
        last_name="McRoll",
        email="johnmcroll@gmail.com",
        gender="Male",
        ip_address="192.168.0.1",
        phone_number="5585992665347",
    )
    await repo_insert_contact(test_session, contact)
    query = text("select * from contact")
    results = await test_session.execute(query)

    contacts = [Contact(**result) for result in results.mappings()]

    assert len(contacts) == 3
    assert contacts[0].first_name == "Emily"
    assert contacts[2].first_name == "John"
    stmt = delete(Contact)
    await test_session.execute(stmt)
    await test_session.commit()
