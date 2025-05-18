from sqlalchemy.orm import Session

def receive_coordinates(lat: float, lon: float):
    # Traitement futur ici si besoin
    print(f"Received coordinates: {lat}, {lon}")
    return "ok"
