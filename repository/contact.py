from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from models.contact import Contact


async def repo_retrieve_contacts(session: AsyncSession, q: str) -> list[Contact]:
    if q == "":
        # If a query param is not provided, return all contacts
        query = text("select * from contact order by first_name")
        results = await session.execute(query)

    else:
        query = text(
            "select * from contact where to_tsvector('english', first_name)"
            " @@ plainto_tsquery('english', :query) order by first_name"
        )
        results = await session.execute(query, {"query": q})

    return [Contact(**result) for result in results.mappings()]


async def repo_insert_contact(session: AsyncSession, contact: Contact):
    session.add(contact)
    await session.commit()
