from datetime import datetime
from typing import Type

from pydantic import BaseModel, HttpUrl


class UserBase(BaseModel):
    id: int
    name: str
    username: str


class UserCreate(UserBase):
    password: str
    photo: str
    phone: str
    url: HttpUrl
    about_me: str
    create_at: datetime

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    photo: str
    phone: str
    url: HttpUrl
    about_me: str

    class Config:
        orm_mode = True