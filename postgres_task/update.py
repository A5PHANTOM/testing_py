from db import sessionLocal,Base
from models import Teacher

session = sessionLocal()

teacher = session.query(Teacher).filter(Teacher.name == "REGHA").first()
teacher.subject = "TAMIL"


session.commit()
session.close()