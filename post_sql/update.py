from db import sessionLocal,Base
from models import Student

session = sessionLocal()


student = session.query(Student).filter(Student.id == 5).first()
student.name = "ANASWARA"

session.commit()
session.close()