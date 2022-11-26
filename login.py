from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI
from db import user_collection

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

