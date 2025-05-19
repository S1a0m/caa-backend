from pydantic import BaseModel
from typing import Optional
from enum import Enum


class BeginColorCycle(str, Enum):
    red = "r"
    orange = "o"
    green = "g"


class TrafficLightBase(BaseModel):
    latitude: float
    longitude: float
    traffic_light_cycle: int
    red_cycle: int
    orange_cycle: int
    green_cycle: int
    begin_color_cycle: Optional[BeginColorCycle] = BeginColorCycle.orange
    turn_right_if_red: Optional[bool] = False
    speed_limit: Optional[int] = 60


class TrafficLightCreate(TrafficLightBase):
    crossroad_id: int


class TrafficLightRead(TrafficLightBase):
    id: int
    crossroad_id: int
    create_at: float 

    class Config:
        orm_mode = True
