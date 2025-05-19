from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schema_user
from app.routes.deps.dependencies import get_db
from app.services.mca import send_confirmation_email

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
    if user: # + matricule ok
        return {"found": True, "matricule": user.matricule}
    return {"found": False}

@router.post("/vehicle/confirm-plate-change/{user_email}")
def send_plate_change_email(user_email: str):
    confirmation_link = f"https://ton-site.com/confirm-plate?email={user_email}"
    send_confirmation_email(to_email=user_email, confirmation_url=confirmation_link)
    return {"message": "Email de confirmation envoyé"}

@router.get("/confirm-plate")
def confirm_plate(email: str = Query(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # mettre à jour "plate_change_confirmed"
    # user.plate_change_confirmed = True
    # db.commit()

    return {
        "message": f"Bonjour {user.name}, votre demande de modification de plaque a bien été confirmée."
    }