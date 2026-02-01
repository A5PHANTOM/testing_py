from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session

from models import Student
from db import sessionLocal
from schema import ReadStudent ,WriteStudent

app = FastAPI()

def get_db ():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/student",response_model=ReadStudent)
def creta_student(
    student: WriteStudent,
    db : Session = Depends(get_db)):

    new_student = Student(
    name = student.name,
    subject = student.subject
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students",response_model=list[ReadStudent])
def get_students(db :  Session = Depends(get_db)):
   return db.query(Student).all()


@app.get("/students/{student_id}",response_model=ReadStudent)
def get_student(student_id : int , db : Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student :
        raise HTTPException (status_code= 404,detail="Student not found")
    return student