import pytest
from api.router import retrieve_contacts


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
