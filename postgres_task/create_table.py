from db import engine,Base
from models import Teacher

Base.metadata.create_all(engine)