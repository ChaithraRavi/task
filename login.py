from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI
from passlib.context import CryptContext

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

