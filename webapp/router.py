import logging
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.async_db import get_session
from api.router import retrieve_contacts as api_retrieve_contacts
from api.router import insert_contact as api_insert_contacts
from models.contact import Contact

logging.basicConfig(level=logging.DEBUG)


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=RedirectResponse)
async def root():
    return "/contacts"


@router.get("/contacts", response_class=HTMLResponse)
async def retrieve_contacts(
    request: Request, session: AsyncSession = Depends(get_session), q: str = ""
):
    logging.debug("Passei aqui")
    results = await api_retrieve_contacts(session, q)

    return templates.TemplateResponse(
        request, "contacts.html", {"q": q, "results": results}
    )


@router.get("/contacts/new", response_class=HTMLResponse)
async def show_contact_form(request: Request):
    return templates.TemplateResponse(
        request, "new.html", {"contact": None, "error": ""}
    )


@router.post("/contacts/new", response_class=RedirectResponse)
async def insert_contact(
    request: Request,
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    try:
        contact = Contact(
            email=email, first_name=first_name, last_name=last_name, phone_number=phone
        )
        inserted = await api_insert_contacts(contact, session)
        message = "Contact saved successfully!"

        return templates.TemplateResponse(
            request, "contacts.html", {"contact": inserted, "message": message}
        )
    except Exception as e:
        return templates.TemplateResponse(
            request, "contacts.html", {"contact": contact, "error": repr(e)}
        )
