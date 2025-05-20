from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schema_user
from app.models import user as model_user
from app.routes.deps.dependencies import get_db

router = APIRouter(prefix="/users", tags=["Utilisateurs enregistrés"])


@router.post("/", response_model=schema_user.UserCreate)
def create_sanctions(sanction: schema_user.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, sanction)