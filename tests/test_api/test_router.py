import pytest

from api.router import retrieve_contacts, insert_contact
from models.contact import Contact


@pytest.mark.asyncio
async def test_retrieve_contacts_with_q(session):
    contacts = await retrieve_contacts(session, "Emily")

    assert contacts is not None
    assert len(contacts) == 1


@pytest.mark.asyncio
async def test_retrieve_contacts_without_q(session):
    contacts = await retrieve_contacts(session)

    assert contacts is not None
    assert len(contacts) == 2


@pytest.mark.asyncio
async def test_insert_contact(session):
    contact = Contact(
        first_name="John",
        last_name="McRoll",
        email="johnmcroll@gmail.com",
        gender="Male",
        ip_address="192.168.0.1",
        phone_number="5585992665347",
    )

    assert contact.id is None

    result = await insert_contact(contact, session)

    assert result is not None
    assert result.id is not None
