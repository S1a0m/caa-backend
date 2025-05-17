from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_sanctions():
    return [{"id": 1, "type": "Retard"}, {"id": 2, "type": "Absence"}]
