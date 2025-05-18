from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schema_user
from app.routes.deps.dependencies import get_db

router = APIRouter()

@router.get("/user/{matricule}", response_model=schema_user.UserInDB)
def get_user(matricule: str, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_matricule(db, matricule)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/matricule/{matricule}")
def check_matricule(matricule: str, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_matricule(db, matricule)
    if user:
        return {"found": True, "matricule": user.matricule}
    return {"found": False}
