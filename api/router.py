from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.async_db import get_session
from repository.contact import repo_retrieve_contacts, repo_insert_contact
from models.contact import Contact


router = APIRouter()


@router.get("/contacts", response_model=list[Contact])
async def retrieve_contacts(session: AsyncSession = Depends(get_session), q: str = ""):
    return await repo_retrieve_contacts(session, q)


@router.post("/contacts/new", response_model=Contact)
async def insert_contact(
    contact: Contact, session: AsyncSession = Depends(get_session)
):
    await repo_insert_contact(session, contact)
    await session.refresh(contact)

    return contact
