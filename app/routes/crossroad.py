from fastapi import APIRouter
from app.schemas.crossroad import GPSCoordinates
from app.crud.crossroad import receive_coordinates

router = APIRouter()

@router.post("/gps")
def handle_gps(coords: GPSCoordinates):
    return {"status": receive_coordinates(coords.latitude, coords.longitude)}
