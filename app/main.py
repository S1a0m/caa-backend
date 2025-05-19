from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sanctions, crossroad, vehicle, traffic_light
from dotenv import load_dotenv

from app.routes import vehicle
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
# app.include_router(vehicle.router, prefix="/user", tags=["User"])
app.include_router(sanctions.router)
app.include_router(vehicle.router)
app.include_router(crossroad.router)
app.include_router(traffic_light.router)

@app.get("/")
def root():
    return {"Connected": True}
