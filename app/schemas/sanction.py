from pydantic import BaseModel

class SanctionBase(BaseModel):
    title: str
    description: str

class SanctionCreate(SanctionBase):
    pass

class SanctionRead(SanctionBase):
    id: int

    class Config:
        orm_mode = True
