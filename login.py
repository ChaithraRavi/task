from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI
from db import user_collection

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

class middleware:
    def func(username,password):
        user = user_collection.find_one({"name": username})
        if user['password'] == password:
            return "success"
        else:
            return "failed"
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            print("agds")
        )
        
    @classmethod
    def validate(cls, v):
        pass

    def __repr__(self):
        return f'PostCode({super().__repr__()})'