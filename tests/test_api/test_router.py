import pytest
from api.router import retrieve_contacts


@pytest.mark.asyncio
async def test_retrieve_contacts(session):
    contacts = await retrieve_contacts(session, "Linda")

    assert contacts is not None
    assert len(contacts) == 2
