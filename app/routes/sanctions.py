from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import sanction as crud_sanction
from app.schemas import sanction as schema_sanction
from app.routes.deps.dependencies import get_db

router = APIRouter()

@router.get("/sanctions", response_model=list[schema_sanction.Sanction])
def read_sanctions(db: Session = Depends(get_db)):
    return crud_sanction.get_sanctions(db)
