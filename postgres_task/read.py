from db import sessionLocal,Base
from models import Teacher

session = sessionLocal()

teacher = session.query(Teacher).all()


for s in teacher:
    print(s.id,s.name,s.subject)

    