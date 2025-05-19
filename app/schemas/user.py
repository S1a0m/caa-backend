from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    surname: str
    address: str
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
