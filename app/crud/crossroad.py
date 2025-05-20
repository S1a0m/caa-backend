from sqlalchemy.orm import Session
from app.models import crossroad as models_crossroad
from app.schemas import crossroad as schemas_crossroad

def get_crossroads_coordinates(db: Session):
    return db.query(models_crossroad.Crossroad).all()

def register_crossroad(db: Session, crossroad: schemas_crossroad.CrossroadCreate):
    db_crossroad = models_crossroad.Crossroad(**crossroad.dict())
    db.add(db_crossroad)
    db.commit()
    db.refresh(db_crossroad)
    return db_crossroad