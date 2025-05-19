from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..core.database import Base

class Crossroad(Base):
    __tablename__ = "crossroads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    traffic_lights = relationship("TrafficLight", back_populates="crossroad")
