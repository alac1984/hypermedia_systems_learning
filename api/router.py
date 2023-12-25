from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.async_db import get_session


router = APIRouter()


# Dummy root endpoint, delete it
@router.get("/", response_class=HTMLResponse)
async def root(request: Request, session: AsyncSession = Depends(get_session)):
    return {"hello": "world"}
