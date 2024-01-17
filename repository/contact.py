from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from models.contact import Contact


async def repo_retrieve_contacts(session: AsyncSession, q: str = "") -> list[Contact]:
    query = text(
        "select * from contact where to_tsvector('english', first_name)"
        " @@ plainto_tsquery('english', :query)"
    )
    results = await session.execute(query, {"query": q})

    return [Contact(**result) for result in results.mappings()]
