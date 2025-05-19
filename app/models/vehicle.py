from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from ..core.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    permitted = Column(Boolean, default=False) # contrôlé et donc peut démarrer

    owner = relationship("User", back_populates="vehicles")
