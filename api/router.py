from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.async_db import get_session
from repository.contact import repo_retrieve_contacts
from models.contact import Contact


router = APIRouter()


@router.get("/contacts", response_model=list[Contact])
async def retrieve_contacts(session: AsyncSession = Depends(get_session), q: str = ""):
    return await repo_retrieve_contacts(session, q)
