from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Sanction(Base):
    __tablename__ = "sanctions"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
