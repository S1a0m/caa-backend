from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    matricule: str

class UserCreate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
