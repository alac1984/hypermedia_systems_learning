from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime


class Base(SQLModel, table=False):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    created: datetime = Field(default=datetime.utcnow(), sa_column=Column(DateTime(timezone=True)))
    modified: datetime = Field(default=datetime.utcnow(), sa_column=Column(DateTime(timezone=True)))
