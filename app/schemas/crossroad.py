from pydantic import BaseModel

class GPSCoordinates(BaseModel):
    latitude: float
    longitude: float
