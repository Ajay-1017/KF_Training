from pydantic import BaseModel , ConfigDict ,Field , EmailStr

from datetime import datetime

class StudentBase(BaseModel):
    name : str = Field(min_length=1 , max_length=50)
    email : EmailStr = Field(max_length = 50)
    age : int 
    department : str = Field(min_length=1)

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    name : str | None = Field( default=None , min_length =1 , max_length= 50 )
    email : EmailStr | None = Field(default=None)
    age : int | None = Field(default=None)
    department : str | None = Field(default=None , min_length=1)


class StudentResponse(StudentBase):
    model_config = ConfigDict(from_attributes = True) 
    id : int
    created_at : datetime

    




