import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str):
    return {
        "access_token" : token
    }
    
def signJWT(name: str):
    payload = {
        "name": name,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm = JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    decodetoken = jwt.decode(token,JWT_SECRET,algorithm = JWT_ALGORITHM)
    return decodetoken if decodetoken['expires'] >= time.time() else None
