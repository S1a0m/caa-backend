from sqlalchemy.orm import Session
from app.models import traffic_light as models_traffic_light
from app.schemas import traffic_light as schemas_traffic_light

def get_trafic_light_state(db: Session, id_tl: str):
    return db.query(models_traffic_light.TrafficLight).filter(models_traffic_light.TrafficLight.id == id_tl).first()

def get_traffic_lights_by_crossroad(db: Session, crossroad_id: int) -> list[models_traffic_light.TrafficLight]:
    return db.query(models_traffic_light.TrafficLight).filter(models_traffic_light.TrafficLight.crossroad_id == crossroad_id).all()

def get_traffic_lights(db: Session):
    return db.query(models_traffic_light.TrafficLight).all()

def create_traffic_light(db: Session, tl: schemas_traffic_light.TrafficLightCreate):
    db_tl = models_traffic_light.TrafficLight(**tl.dict())
    db.add(db_tl)
    db.commit()
    db.refresh(db_tl)
    return db_tl