from pydantic import BaseModel, EmailStr , ConfigDict, Field ,field_validator, model_serializer
from fastapi import Form
from enum import Enum


class LoginForm:
    def __init__(
        self,
        username: str = Form(...),
        password: str = Form(...),
    ):
        self.username = username
        self.password = password



class RoleChoice(str,Enum):
    ADMIN = "admin"
    USER = "user"

# Flow 

# FRONTEND
#    │
#    │ JSON
#    │
#    │ {"role": "admin"}
#    ↓
# FASTAPI
#    │
#    ↓
# PYDANTIC
#    │
#    │ Schema says:
#    │ role: RoleChoice
#    ↓
# RoleChoice
#    │
#    ├── ADMIN → "admin"
#    └── USER  → "user"
#    │
#    ↓
# Compare incoming "admin"
#    │
#    ├── matches "admin" → ✅
#    │
#    └── doesn't match   → ❌ ValidationError
#    │
#    ↓
# Python object
#    │
#    ↓
# role = RoleChoice.ADMIN
#    │
#    └── role.value → "admin"



# user create 
class UserBase(BaseModel):

    email : EmailStr = Field(max_length=50)
    is_active : bool = Field(default=True)



class UserInfoBase(BaseModel):

    full_name : str = Field(max_length=50)

    phone : str = Field(
        min_length=10, 
        max_length=10,
        pattern = r"^\d+$",
    )

    role : RoleChoice   

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls,value : str):
        if not value.strip():
            raise ValueError("full name cannot not be empty")
        return value.strip() 


class UserCreate (UserBase):

    password : str = Field(min_length=8)

    user_info : UserInfoBase

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str):
        if not value.strip():
            raise ValueError("password cannot be empty")
        return value


class UserInfoUpdateBase(BaseModel):

    full_name : str | None = Field(default=None,max_length=50)

    phone : str | None = Field(
        default=None,
        min_length=10, 
        max_length=10,
        pattern = r"^\d+$"
    )   

    role: RoleChoice | None = None

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls,value : str | None):
        if value is not None and not value.strip():
            raise ValueError("full name cannot not be empty")
        return value 



class UserUpdateBase(BaseModel):
    email : EmailStr | None = Field(default = None , max_length=50)
    password : str   | None = Field(default=None,min_length=8)
    is_active : bool | None = None

    @field_validator("password")
    @classmethod
    def validate_password(cls, value : str | None):
        if value is not None and not value.strip():
            raise ValueError("password cannot be empty")
        return value


class UserUpdate (UserUpdateBase):
    user_info: UserInfoUpdateBase | None = None





# --------------- User Response------------------

def mask_email(email : str) -> str:
    local , domain = email.split("@")
    domain_name , extension = domain.rsplit(".",1)

    masked_local = local[:2] + "***"
    masked_domain = "***." + extension

    return f"{masked_local}@{masked_domain}"


def mask_phone(password : str) -> str :
    return password[:2] + "******" + password[-2:]



class UserResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    public_id : str 
    email : str
    is_active : bool 

    
class UserInfoResponseBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    full_name : str 
    phone : str
    role : RoleChoice

    @model_serializer
    def serialize_model(self):
        return{
            "fullName" : self.full_name,
            "phone" : mask_phone(self.phone),
            "role" : self.role
         }

class UserResponse(UserResponseBase):
    user_info : UserInfoResponseBase

    @model_serializer
    def serialize_model(self):
        return{
            "publicId" : self.public_id,
            "email" : mask_email(self.email),
            "isActive" : self.is_active,
            "userInfo" : self.user_info
         }









