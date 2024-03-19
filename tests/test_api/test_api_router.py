import pytest

from api.router import retrieve_contacts, insert_contact
from models.contact import Contact


@pytest.mark.asyncio
async def test_api_retrieve_contacts_with_q(test_session):
    contacts = await retrieve_contacts(test_session, "Emily")

    assert len(contacts) == 1


@pytest.mark.asyncio
async def test_api_retrieve_contacts_without_q(test_session):
    contacts = await retrieve_contacts(test_session)

    assert len(contacts) == 2


@pytest.mark.asyncio
async def test_api_insert_contact(test_session):
    contact = Contact(
        first_name="John",
        last_name="McRoll",
        email="johnmcroll@gmail.com",
        gender="Male",
        ip_address="192.168.0.1",
        phone_number="5585992665347",
    )

    assert contact.id is None

    result = await insert_contact(contact, test_session)

    assert result.id is not None
