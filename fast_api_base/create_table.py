from db import sessionLocal,Base,engine
from models import Student

Base.metadata.create_all(engine)