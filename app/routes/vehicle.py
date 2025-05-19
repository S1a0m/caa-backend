from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.crud import vehicle as crud_vehicle
from app.schemas import vehicle as schema_vehicle
from app.routes.deps.dependencies import get_db
from app.services.mca import send_confirmation_email

router = APIRouter(prefix="/vehicle", tags=["Véhicules enregistrés"])

@router.get("/{plate_number}", response_model=schema_vehicle.VehicleRead)
def check_plate_number_right(plate_number: str, db: Session = Depends(get_db)):
    vehicle = crud_vehicle.get_vehicle_by_matricule(db, plate_number)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Un véhicule portant cette plaque n'existe pas.")
    return vehicle

@router.get("/plate_number/{plate_number}")
def record_use_plate_number(plate_number: str, db: Session = Depends(get_db)):
    vehicle = crud_vehicle.get_vehicle_by_matricule(db, plate_number)
    if vehicle: 
        user = crud_user.get_user_by_vehicle_plate(db, plate_number)
        confirmation_link = f"http://localhost:8000/vehicle/confirm-plate/{plate_number}"
        send_confirmation_email(to_email=user.email, confirmation_url=confirmation_link, receiver_name=user.name, receiver_surname=user.surname, vehicle_plate_number=plate_number)
        return {"found": True}
    return {"found": False}

@router.get("/confirm-plate/{plate_number}") 
def confirm_plate(plate_number: str, db: Session = Depends(get_db)):
    vehicle = crud_vehicle.get_vehicle_by_matricule(db, plate_number)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Modification impossible.")

    vehicle.permitted = True
    db.commit()
    db.refresh(vehicle)

    return {"message": f"Modification effectuée pour {plate_number}."}
