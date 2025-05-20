from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.crossroad import CrossroadBase, CrossroadCreate
from app.crud.crossroad import get_crossroads_coordinates, register_crossroad
from app.crud.traffic_light import get_traffic_lights_by_crossroad, get_trafic_light_state
from app.routes.deps.dependencies import get_db
from app.utils.geolocalisation import haversine, find_nearest_point

router = APIRouter(prefix="/gps", tags=["GPS Géolocalisation"])

@router.post("/")
def handle_gps(coords: CrossroadBase, db: Session = Depends(get_db)):
    user_location = (coords.latitude, coords.longitude)

    # Étape 1: Récupérer tous les carrefours
    crossroads = get_crossroads_coordinates(db)
    if not crossroads:
        raise HTTPException(status_code=404, detail="Aucun carrefour trouvé.")

    # Étape 2: Trouver le carrefour le plus proche
    crossroad_points = [(c.latitude, c.longitude) for c in crossroads]
    nearest_crossroad_point = find_nearest_point(user_location, crossroad_points)

    if not nearest_crossroad_point:
        return {"status": False, "message": "Aucun carrefour proche."}

    matched_crossroad = next(
        (c for c in crossroads if (c.latitude, c.longitude) == nearest_crossroad_point), None
    )
    if not matched_crossroad:
        return {"status": False, "message": "Carrefour introuvable."}

    # Étape 3: Récupérer les feux tricolores associés
    traffic_lights = get_traffic_lights_by_crossroad(db, matched_crossroad.id)
    if not traffic_lights:
        return {"status": False, "message": "Aucun feu tricolore à ce carrefour."}

    # Étape 4: Identifier le feu le plus proche
    tl_points = [(tl.latitude, tl.longitude) for tl in traffic_lights]
    nearest_tl_point = find_nearest_point(user_location, tl_points)

    nearest_tl = next(
        (tl for tl in traffic_lights if (tl.latitude, tl.longitude) == nearest_tl_point), None
    )
    if not nearest_tl:
        return {"status": False, "message": "Aucun feu proche trouvé."}

    # Étape 5: Vérifier que le feu est à moins de 200 mètres
    distance = haversine(user_location[0], user_location[1], nearest_tl.latitude, nearest_tl.longitude)
    if distance > 0.2:  # 200 mètres
        return {"status": False} # "Feu trop éloigné (> 200 m)."

    # Étape 6: Récupérer l’état du feu
    state = get_trafic_light_state(db, nearest_tl.id)

    return {
        "status": True,
        "crossroad_name": matched_crossroad.name,
        "traffic_light_id": nearest_tl.id,
        "distance_m": round(distance * 1000, 2),
        "state": state
    }

@router.post("/crossroad", response_model=CrossroadCreate)
def create_crossroad(crossroad: CrossroadCreate, db: Session = Depends(get_db)):
    return register_crossroad(db, crossroad)