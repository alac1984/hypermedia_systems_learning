import pytest
from fastapi.requests import Request
from jinja2.environment import Template

from webapp.router import retrieve_contacts, insert_contact


@pytest.mark.asyncio
async def test_webapp_get_retrieve_contacts(test_session):
    request = Request(scope={"type": "http"})
    response = await retrieve_contacts(request, test_session)

    assert response is not None
    assert response.status_code == 200
    assert isinstance(response.template, Template)
    assert response.template.name == "contacts.html"


@pytest.mark.asyncio
async def test_webapp_get_show_contact_form():
    request = Request(scope={"type": "http"})
    response = await insert_contact(request)

    assert response is not None
    assert response.status_code == 200
    assert isinstance(response.template, Template)
    assert response.template.name == "new.html"


# TODO: test show contact form
