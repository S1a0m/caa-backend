from pydantic import BaseModel
from typing import List


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

