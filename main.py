from fastapi import FastAPI, Depends, Body
from schemas import User, User_details
from db import user_collection, userDetails_collection
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
import random, string
from login import encrypt_password
from helper import user_helper,userDetails_helper
from jwt_handler import signJWT
from jwt_bearer import jwtBearer

app = FastAPI()

def check_user(data: User,user_details):
    if user_details['email'] == data['email'] and user_details['password'] == data['password']:
        return True
    return False
 
def get_otp():
    onetimepwd=''.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
    return ''.join(random.sample(onetimepwd,len(onetimepwd)))


@app.post("/create_user",dependencies=[Depends(jwtBearer())])
async def create_user(user:User):
    user = jsonable_encoder(user)
    hashed_pwd = encrypt_password(user['password'])
    user.update({'password':hashed_pwd})
    otp = get_otp()
    user.update({'otp':otp})
    user_value = await user_collection.insert_one(user)
    new_user = await user_collection.find_one({"_id": user_value.inserted_id})
    return user_helper(new_user)
    

@app.get("/{id}",dependencies=[Depends(jwtBearer())])
async def user(id):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)
    else:    
        return "User not found"


@app.post("/user/signup")
async def user(user: User = Body(...)):
    user = jsonable_encoder(user)
    hashed_pwd = encrypt_password(user['password'])
    user.update({'password':hashed_pwd})
    onetimepwd=''.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
    otp= ''.join(random.sample(onetimepwd,len(onetimepwd)))
    user.update({'otp':otp})
    user_value = await user_collection.insert_one(user)
    import pdb;pdb.set_trace()
    return signJWT(user['name'])    


@app.post("/user/login")
async def user_login(user: User = Body(...)):
    user = jsonable_encoder(user)
    user_details = await user_collection.find_one({"email": user['email']})
    if check_user(user,user_details):
        return signJWT(user['email'])
    return {
        "error": "Wrong login details!"
    }
    
    
@app.put("userDetails_update/{id}",dependencies=[Depends(jwtBearer())])
async def update(id,user_model:User_details):
    user = await userDetails_collection.find_one({"_id": ObjectId(id)})
    req = {k: v for k, v in user_model.dict().items() if v is not None}
    if not user:
        "User not found"
    else:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": req}
        )
    return userDetails_helper(user)


@app.delete("/{id}",dependencies=[Depends(jwtBearer())])
async def delete(id: str):
    await user_collection.delete_one({"_id": ObjectId(id)})
    return True
