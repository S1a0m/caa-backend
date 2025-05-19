from sqlalchemy.orm import Session
from app.models import crossroad
from app.schemas import crossroad

def get_crossroads_coordinates(db: Session):
    return db.query(crossroad.Crossroad).all()

def register_crossroad(db: Session, sanction: crossroad.CroosroadCreate):
    db_crossroad = crossroad.Crossroad(**sanction.dict())
    db.add(db_crossroad)
    db.commit()
    db.refresh(db_crossroad)
    return db_crossroad