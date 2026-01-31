from db import sessionLocal,Base
from sqlalchemy import Integer,String,Column

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer,primary_key=True)
    name =Column(String,nullable=False)
    subject= Column(String,nullable=False)
    

