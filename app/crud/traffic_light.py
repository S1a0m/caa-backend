from sqlalchemy.orm import Session
from app.models import traffic_light
from app.schemas import traffic_light

def get_trafic_light_state(db: Session, id_tl: str):
    return db.query(traffic_light).filter(traffic_light.TrafficLight.id == id_tl).first()

def get_traffic_lights_by_crossroad(db: Session, crossroad_id: int) -> list[traffic_light.TrafficLight]:
    return db.query(traffic_light.TrafficLight).filter(traffic_light.TrafficLight.crossroad_id == crossroad_id).all()

def create_traffic_light(db: Session, tl: traffic_light.TrafficLightCreate):
    db_tl = traffic_light.TrafficLight(**tl.dict())
    db.add(db_tl)
    db.commit()
    db.refresh(db_tl)
    return db_tl