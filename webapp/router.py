from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.async_db import get_session
from api.router import retrieve_contacts


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# Dummy root endpoint, delete it


@router.get("/", response_class=RedirectResponse)
async def root(request: Request):
    return "/contacts"


@router.get("/contacts", response_class=HTMLResponse)
async def contacts(
    request: Request, session: AsyncSession = Depends(get_session), q: str = ""
):
    results = await retrieve_contacts(session, q)

    return templates.TemplateResponse(
        "contacts.html", {"request": request, "q": q, "results": results}
    )
