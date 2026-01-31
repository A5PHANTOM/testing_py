#3 

from db import engine,Base
from models import Student

Base.metadata.create_all(engine)

