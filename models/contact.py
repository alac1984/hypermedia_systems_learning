from pydantic import EmailStr, IPvAnyAddress
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlmodel import Field
from sqlalchemy import Column, String

from .base import Base


class Contact(Base, table=True):
    first_name: str
    last_name: str
    email: EmailStr = Field(sa_column=Column(String))
    gender: str
    ip_address: IPvAnyAddress = Field(sa_column=Column(String))
    phone_number: PhoneNumber = Field(sa_column=Column(String))
