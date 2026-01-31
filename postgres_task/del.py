from db import sessionLocal,Base
from models import Teacher

session = sessionLocal()

teacher = session.query(Teacher).filter(Teacher.name == 'JASIM').first()
session.delete(teacher)


session.commit()
session.close()