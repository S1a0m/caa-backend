from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import traffic_light as crud_traffic_light
from app.schemas import traffic_light as schema_traffic_light
from app.routes.deps.dependencies import get_db

router = APIRouter(prefix="/traffic-light", tags=["Feux tricolores enregistrés"])

@router.get("/", response_model=list[schema_traffic_light.TrafficLightRead])
def read_traffic_lights(db: Session = Depends(get_db)):
    return crud_traffic_light.get_traffic_lights(db)


@router.post("/", response_model=schema_traffic_light.TrafficLightCreate)
def create_traffic_light(tl: schema_traffic_light.TrafficLightCreate, db: Session = Depends(get_db)):
    return crud_traffic_light.create_traffic_light(db, tl)