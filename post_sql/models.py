#2
from sqlalchemy import Column,Integer,String

from db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    course = Column(String, nullable= False)


