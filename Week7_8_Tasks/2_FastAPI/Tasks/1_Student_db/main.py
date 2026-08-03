from typing import Annotated

from fastapi import FastAPI , Depends  , status
from fastapi.exceptions import HTTPException


from Tasks.Student_db.database import engine , get_db , Base 

from sqlalchemy import select 
from sqlalchemy.orm import Session

from Tasks.Student_db.schemas import StudentResponse ,StudentCreate , StudentUpdate

import Tasks.Student_db.models as models

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def home():
    return {"message" : "welcome to student db"}

@app.get("/health")
def health():
    return {
        "message" : "health status"
    }

@app.post("/api/student" , response_model = StudentResponse)
def create_student( student : StudentCreate , db : Annotated[Session , Depends(get_db)]):

    result = db.execute(
        select(models.Student).where(models.Student.email == student.email)
    )

    existing_email = result.scalars().first()

    if existing_email:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST , 
            detail = f"{existing_email.email} already exist"
        )

    new_std = models.Student(
        name = student.name,
        email = student.email,
        age = student.age,
        department = student.department
    )

    db.add(new_std)
    db.commit()

    return new_std


@app.get("/api/students" , response_model= list[StudentResponse])
def get_students(db : Annotated[Session , Depends(get_db)]):
    result = db.execute(
        select(models.Student)
    )
    students = result.scalars().all()
    return students

@app.get("/api/students/{student_id}" , response_model= StudentResponse)
def get_student(student_id : int , db : Annotated[Session , Depends(get_db)]):
    result = db.execute(
        select(models.Student).where(models.Student.id == student_id )
    )
    student = result.scalars().first()
    if student:
        return student
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "id is not exist"
    )

@app.patch("/api/students/{student_id}" , response_model=StudentResponse)
def update_student(student_update : StudentUpdate , student_id : int , db : Annotated[Session , Depends(get_db)]):

    result  = db.execute(
        select(models.Student).where( models.Student.id == student_id )
    )

    student = result.scalars().first()

    if not student:
        raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "id is not exist"
    )

    if student.email is not None and student.email != student_update.email:

        result = db.execute(
            select(models.Student).where(models.Student.email == student_update.email)
        )

        existing_email = result.scalars().first()

        if existing_email :
            raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = "email id already exist"
                )

    update_student = student_update.model_dump(exclude_unset=True)

    for field , value in update_student.items():
        setattr(student , field , value)

    db.commit()
    db.refresh(student)
    
    return student

@app.delete("/api/students/{student_id}",
            status_code=status.HTTP_204_NO_CONTENT
            )
def delete_student(
    student_id : int, 
    db : Annotated[Session , Depends(get_db)]
):
    result = db.execute(
        select(models.Student).where(models.Student.id == student_id)
    )

    student = result.scalars().first()

    if not student:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "student id not found"
        )

    db.delete(student)
    db.commit()


        
    
