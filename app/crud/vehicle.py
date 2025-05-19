from sqlalchemy.orm import Session
from app.models import vehicle 
from app.schemas import user 

def get_vehicle_by_matricule(db: Session, plate_number: str):
    return db.query(vehicle.Vehicle).filter(vehicle.Vehicle.plate_number == plate_number).first()

