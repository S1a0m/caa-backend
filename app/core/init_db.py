from app.core.database import Base, engine
from app.models import sanction, user, vehicle, crossroad

Base.metadata.create_all(bind=engine)