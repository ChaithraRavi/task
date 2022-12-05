from pydantic import BaseModel, EmailStr

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
                "user": "userID",
                "age": 12,
                "phone_number": "9438899000",
                "otp":  "ks234",
                "path": "user/oneverse"
            }
        }


