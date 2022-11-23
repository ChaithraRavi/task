from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    name : str
    password : str
    email : EmailStr
    is_active : bool
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
    age: int
    phone_number: str
    otp:  str
    path: str
    class Config:
        schema_extra = {
            "example": {
                "user": "user",
                "age": 12,
                "phone_number": "9438899000",
                "otp":  "ks234",
                "path": "user/oneverse"
            }
        }
        
        
def user_helper(user) -> dict:
    return {
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
        "is_active": user["is_active"]
    }

def userDetails_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "age": user["age"],
        "phone_number": user["phone_number"],
        "password": user["name"],
        "otp": user["otp"],
        "path": user["path"]
    }
