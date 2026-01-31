from db import sessionLocal,Base
from models import Student

sesssion = sessionLocal()

students = sesssion.query(Student).all()

for s in students:
    print(s.id,s.name,s.course)

sesssion.close()

