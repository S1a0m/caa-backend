from pydantic import BaseModel
from datetime import datetime

class SanctionBase(BaseModel):
    reason: str
    amount: float

class SanctionCreate(SanctionBase):
    user_id: int

class Sanction(SanctionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
