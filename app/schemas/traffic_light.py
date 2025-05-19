from pydantic import BaseModel
from typing import Optional


class TrafficLightBase(BaseModel):
    latitude: float
    longitude: float


class TrafficLightCreate(TrafficLightBase):
    crossroad_id: int  # à quel carrefour rattacher le feu


class TrafficLightRead(TrafficLightBase):
    id: int
    crossroad_id: int

    class Config:
        orm_mode = True
