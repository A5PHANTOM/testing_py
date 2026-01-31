from db import sessionLocal,Base
from models import Teacher

session = sessionLocal()


teacher1 = Teacher(name = "JASIM" , subject = "CS")
teacher2 = Teacher(name = "REGHA",subject = "HINDI")

session.add_all([teacher1,teacher2])

session.commit()
session.close()