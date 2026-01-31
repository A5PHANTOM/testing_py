from db import sessionLocal
from models import Student

sesssion = sessionLocal()

student1 = Student(name = "DEVIKA", course = "Btech")
student2 = Student(name = "GEETHIKA", course = "Mtech")

sesssion.add_all([student1,student2])
sesssion.commit()
sesssion.close()