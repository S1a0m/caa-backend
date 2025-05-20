from sqlalchemy.orm import Session
from app.models import user, vehicle  
from app.schemas import user as schemas_user
from typing import Optional

def get_user_by_vehicle_plate(db: Session, plate_number: str) -> Optional[user.User]:
    return db.query(user.User).join(vehicle.Vehicle).filter(vehicle.Vehicle.plate_number == plate_number).first()


def create_user(db: Session, tl: schemas_user.UserCreate):
    db_tl = user.User(**tl.dict())
    db.add(db_tl)
    db.commit()
    db.refresh(db_tl)
    return db_tl