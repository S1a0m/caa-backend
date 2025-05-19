from sqlalchemy.orm import Session
from app.models import user, vehicle  # Adapte selon ton import
from typing import Optional

def get_user_by_vehicle_plate(db: Session, plate_number: str) -> Optional[user.User]:
    return db.query(user.User).join(vehicle.Vehicle).filter(vehicle.Vehicle.plate_number == plate_number).first()
