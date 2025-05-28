from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os

security = HTTPBearer()
JWT_SECRET = os.getenv("JWT_SECRET", "mysecret")

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(status_code=403, detail="Invalid token")

from fastapi import APIRouter
import datetime

auth_router = APIRouter()

@auth_router.post("/login")
def login():
    payload = {
        "sub": "testuser",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}
