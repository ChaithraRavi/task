from fastapi import FastAPI
from fastapi import APIRouter
# from db import conn
from schemas import User, UpdateUser
from db import user_collection 
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
import random, string
from fastapi import APIRouter, Body


user = APIRouter()
app = FastAPI()

def user_helper(student) -> dict:
    
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "phone_number": student["phone_number"],
        "password": student["name"],
        "otp": student["otp"],
        "path": student["path"]
    }

@app.get("/{id}")
async def user(id):
    student = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(student)

@app.post("/")
async def create(user:User):
    user = jsonable_encoder(user)
    otp=''.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
    otp1= ''.join(random.sample(otp,len(otp)))
    user.update({'otp':otp1})
    student = await user_collection.insert_one(user)
    new_student = await user_collection.find_one({"_id": student.inserted_id})
    return user_helper(new_student)


@app.delete("/{id}")
async def delete(id: str):
    await user_collection.delete_one({"_id": ObjectId(id)})
    return True
        

@app.put("/{id}")
async def update(id,updateUser: UpdateUser):
    student = await user_collection.find_one({"_id": ObjectId(id)})
    req = {k: v for k, v in updateUser.dict().items() if v is not None}
    if student:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": req}
        )
    return user_helper(student)
     