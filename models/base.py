from sqlmodel import SQLModel, Field
from datetime import datetime


class Base(SQLModel, table=False):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    created: datetime = datetime.now()
    modified: datetime = datetime.now()
