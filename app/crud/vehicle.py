from sqlalchemy.orm import Session
from app.models import vehicle 
from app.schemas import vehicle as schemas_vehicle

def get_vehicle_by_matricule(db: Session, plate_number: str):
    return db.query(vehicle.Vehicle).filter(vehicle.Vehicle.plate_number == plate_number).first()

def create_vehicle(db: Session, tl: schemas_vehicle.VehicleCreate):
    db_vcl = vehicle.Vehicle(**tl.dict())
    db.add(db_vcl)
    db.commit()
    db.refresh(db_vcl)
    return db_vcl