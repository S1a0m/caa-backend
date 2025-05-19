from pydantic import BaseModel
from typing import List
from app.schemas.traffic_light import TrafficLightRead


class CrossroadBase(BaseModel):
    name: str
    latitude: float
    longitude: float


class CrossroadCreate(CrossroadBase):
    pass


class CrossroadRead(CrossroadBase):
    id: int
    traffic_lights: List[TrafficLightRead] = []  # Liste des feux associés

    class Config:
        orm_mode = True

