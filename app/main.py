# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sanctions  

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(sanctions.router, prefix="/sanctions", tags=["Sanctions"])

@app.get("/")
def root():
    return {"message": "Backend FastAPI prêt 🔥"}
