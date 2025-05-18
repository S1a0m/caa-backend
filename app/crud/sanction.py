from sqlalchemy.orm import Session
from app.models import sanction as models
from app.schemas import sanction as schemas

def get_sanctions(db: Session):
    return db.query(models.Sanction).all()

def create_sanction(db: Session, sanction: schemas.SanctionCreate):
    db_sanction = models.Sanction(**sanction.dict())
    db.add(db_sanction)
    db.commit()
    db.refresh(db_sanction)
    return db_sanction
