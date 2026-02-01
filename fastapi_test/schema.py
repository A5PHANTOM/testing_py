from pydantic import BaseModel
from models import Student

class WriteStudent(BaseModel):
    name : str
    subject : str

class ReadStudent(WriteStudent):
    id : int 

    class Config ():
        orm_mode = True