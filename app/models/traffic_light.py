from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Boolean, Float
from sqlalchemy.orm import relationship
from ..core.database import Base
from datetime import datetime
import enum

class BeginColorCycle(str, enum.Enum):
    red = "r"
    orange = "o"
    green = "g"

class TrafficLight(Base):
    __tablename__ = "traffic_lights"

    id = Column(Integer, primary_key=True, index=True)
    crossroad_id = Column(Integer, ForeignKey("crossroads.id"))

    latitude = Column(Float)
    longitude = Column(Float)

    create_at = Column(DateTime, default=lambda: datetime.utcnow().timestamp())
    traffic_light_cycle = Column(Integer, nullable=False)
    red_cycle = Column(Integer, nullable=False)
    orange_cycle = Column(Integer, nullable=False)
    green_cycle = Column(Integer, nullable=False)

    begin_color_cycle = Column(Enum(BeginColorCycle), default=BeginColorCycle.orange)

    turn_right_if_red = Column(Boolean, default=False)

    speed_limit = Column(Integer, default=60)

    crossroad = relationship("Crossroad", back_populates="traffic_lights")
