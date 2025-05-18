from core.database import Base, engine
from models import sanction, user, vehicle, crossroad

Base.metadata.create_all(bind=engine)