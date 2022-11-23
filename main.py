from fastapi import FastAPI, Depends
from schemas import User, User_details
from db import user_collection, userDetails_collection
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
import random, string
from fastapi.security import OAuth2PasswordRequestForm
from login import oauth2_scheme
from schemas import user_helper, userDetails_helper
app = FastAPI()

    
@app.post("/login/token", tags=["login"])
async def retrieve(form_data: OAuth2PasswordRequestForm=Depends()):
    user = await user_collection.find_one({"name": form_data.username})
    if user['password'] == form_data.password:
        return "success"
    else:
        return "failed"


@app.get("/{id}")
async def user(id):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)
    else:    
        return "User not found"


@app.post("/add_user")
async def create(user:User):
    user = jsonable_encoder(user)
    user_value = await user_collection.insert_one(user)
    new_user = await user_collection.find_one({"_id": user_value.inserted_id})
    return user_helper(new_user)
        

@app.post("/add_userDetails")
async def create(user:User_details,token: str=Depends(oauth2_scheme)):
    user = jsonable_encoder(user)
    onetimepwd=''.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(3))
    otp= ''.join(random.sample(onetimepwd,len(onetimepwd)))
    user.update({'otp':otp})
    user_value = await userDetails_collection.insert_one(user)
    new_user = await userDetails_collection.find_one({"_id": user_value.inserted_id})
    return userDetails_helper(new_user)


@app.delete("/{id}")
async def delete(id: str,token: str=Depends(oauth2_scheme)):
    await user_collection.delete_one({"_id": ObjectId(id)})
    return True


@app.delete("/{id}")
async def delete(id: str,token: str=Depends(oauth2_scheme)):
    await userDetails_collection.delete_one({"_id": ObjectId(id)})
    return True
        

@app.put("/{id}")
async def update(id,user_model:User,token: str=Depends(oauth2_scheme)):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    req = {k: v for k, v in user_model.dict().items() if v is not None}
    if not user:
        "User not found"
    else:
        updated_user = await user.update_one(
            {"_id": ObjectId(id)}, {"$set": req}
        )
    return user_helper(user)


@app.put("/{id}")
async def update(id,user_model:User_details,token: str=Depends(oauth2_scheme)):
    user = await userDetails_collection.find_one({"_id": ObjectId(id)})
    req = {k: v for k, v in user_model.dict().items() if v is not None}
    if not user:
        "User not found"
    else:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": req}
        )
    return userDetails_helper(user)


@app.post("/add_user_auth")
async def create_user_auth(user:User, token: str=Depends(oauth2_scheme)):
    user = jsonable_encoder(user)
    user = await user_collection.insert_one(user)
    if user:
        "User not found"
    else:    
        return user_collection(user)