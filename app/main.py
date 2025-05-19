# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sanctions, user, crossroad, vehicle, traffic_light
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(vehicle.router, prefix="/vehicle", tags=["Vehicle"])
app.include_router(crossroad.router, prefix="/crossroad", tags=["Crossroad"])
app.include_router(traffic_light.router, prefix="/light", tags=["Light"])

@app.get("/")
def root():
    return {"message": "Backend FastAPI prêt 🔥"}
