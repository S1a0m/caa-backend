from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import sanction as crud_sanction
from app.schemas import sanction as schema_sanction
from app.routes.deps.dependencies import get_db

router = APIRouter(prefix="/sanctions", tags=["Sanctions enregistrées"])

@router.get("/", response_model=list[schema_sanction.SanctionRead])
def read_sanctions(db: Session = Depends(get_db)):
    return crud_sanction.get_sanctions(db)

# créer une sanction

@router.post("/", response_model=schema_sanction.SanctionCreate)
def create_sanctions(sanction: schema_sanction.SanctionCreate, db: Session = Depends(get_db)):
    return crud_sanction.create_sanction(db, sanction)