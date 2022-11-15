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

def user_helper(user) -> dict:
    
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "phone_number": user["phone_number"],
        "password": user["name"],
        "otp": user["otp"],
        "path": user["path"]
    }

@app.get("/{id}")
async def user(id):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

@app.post("/")
async def create(user:User):
    user = jsonable_encoder(user)
    onetimepwd=''.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
    otp= ''.join(random.sample(onetimepwd,len(onetimepwd)))
    user.update({'otp':otp})
    user_value = await user_collection.insert_one(user)
    new_user = await user_collection.find_one({"_id": user_value.inserted_id})
    return user_helper(new_user)


@app.delete("/{id}")
async def delete(id: str):
    await user_collection.delete_one({"_id": ObjectId(id)})
    return True
        

@app.put("/{id}")
async def update(id,updateUser: UpdateUser):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    req = {k: v for k, v in updateUser.dict().items() if v is not None}
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": req}
        )
    return user_helper(user)
     