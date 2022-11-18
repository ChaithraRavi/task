from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    name : Optional[str]
    password : Optional[str]
    email : Optional[EmailStr]
    is_active : Optional[bool]
    class Config:
        schema_extra = {
            "example": {
                "name": "abc",
                "password": "akjkshd",
                "email": "abc@gmail.com",
                "is_active" : "True"
            }
        }


class User_details(BaseModel):
    user: User
    age: Optional[int]
    phone_number: Optional[str]
    password: Optional[str]
    otp:  Optional[str]
    path: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "user": "user",
                "age": 12,
                "phone_number": "9438899000",
                "password": "jkabdekjq",
                "otp":  "ks234",
                "path": "user/oneverse"
            }
        }
        
