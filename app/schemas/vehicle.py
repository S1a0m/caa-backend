from pydantic import BaseModel
from typing import Optional


class VehicleBase(BaseModel):
    plate_number: str
    permitted: Optional[bool] = False


class VehicleCreate(VehicleBase):
    user_id: int


class VehicleRead(VehicleBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
