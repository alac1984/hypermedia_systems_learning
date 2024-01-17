import pytest

from repository.contact import repo_retrieve_contacts


@pytest.mark.asyncio
async def test_repo_retrieve_contacts(session):
    contacts = await repo_retrieve_contacts(session, "Linda")

    assert contacts is not None
    assert len(contacts) == 2
