from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session

from db import sessionLocal
from models import Student
from schema import StudentCreate , StudentResponse

app = FastAPI()

def get_db (): # Opens DB session per request. Ensures session is closed. Prevents memory leaks

    db = sessionLocal()
    try :
        yield db 
    finally:
        db.close()

@app.post("/students",response_model=StudentResponse)
def create_student(
    student : StudentCreate,
    db : Session = Depends(get_db)   ):
    
    new_stundent = Student (
        name = student.name,
        course = student.course
    )
    db.add(new_stundent)
    db.commit()
    db.refresh(new_stundent)

    return new_stundent


@app.get("/student/",response_model=list[StudentResponse])
def get_students (db : Session= Depends(get_db)):
    return db.query(Student).all()


@app.get("/students/{student_id}",response_model=StudentResponse)
def get_student(student_id: int , db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student :
        raise HTTPException (status_code=404,details="student not founf")
    return student
