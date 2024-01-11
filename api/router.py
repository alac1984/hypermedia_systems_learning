from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.async_db import get_session
from repository.contact import repo_retrieve_contacts
from models.contact import Contact


router = APIRouter()


# Dummy root endpoint, delete it
@router.get("/contacts", response_model=list[Contact])
async def retrieve_contacts(request: Request, session: AsyncSession = Depends(get_session), q: str = ""):
    return await repo_retrieve_contacts(session, q)

