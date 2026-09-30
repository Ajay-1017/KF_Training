from database import engine, Base
from models import ReviewJob

Base.metadata.create_all(engine)

print("Tables created")