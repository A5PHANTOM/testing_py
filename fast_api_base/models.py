from sqlalchemy import Integer,Column,String
from db import sessionLocal,Base

class Student(Base):
    __tablename__ = "fstudents"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    course = Column(String,nullable=False)

