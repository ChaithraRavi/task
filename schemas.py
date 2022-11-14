from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    phone_number: str
    password: str
    otp:  Optional[str]
    path: Optional[str]

class UpdateUser(BaseModel):
    name: Optional[str]
    age: Optional[int]
    phone_number: Optional[str]
    password: Optional[str]
    otp:  Optional[str]
    path: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "name": "abc",
                "age": 12,
                "phone_number": "9438899000",
                "password": "jkabdekjq",
                "otp":  "ks234",
                "path": "user/oneverse"
            }
        }
