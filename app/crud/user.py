from sqlalchemy.orm import Session
from app.models import user as models
from app.schemas import user as schemas

def get_user_by_matricule(db: Session, matricule: str):
    return db.query(models.User).filter(models.User.matricule == matricule).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(matricule=user.matricule)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
