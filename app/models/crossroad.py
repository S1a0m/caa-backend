from sqlalchemy import Column, Integer, Float
from core.database import Base

class Crossroad(Base):
    __tablename__ = "crossroads"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)