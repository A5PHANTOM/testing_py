from sqlalchemy import Integer,String,Column
from db import Base,sessionLocal

class Student(Base):
    __tablename__ = "schooltab"

    id = Column(Integer ,primary_key=True,index=True)
    name =Column(String,nullable=False)
    subject= Column(String,nullable=False)

    
