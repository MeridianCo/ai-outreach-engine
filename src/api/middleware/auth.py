import jwt as pyjwt
from fastapi import Header, HTTPException

from src.db.queries.read import get_user_id_by_auth_id
from src.db.config import SUPABASE_JWT

def get_current_user(authorization: str = Header(...)):
    token = authorization.removeprefix("Bearer ")

    try:
        payload = pyjwt.decode(token, SUPABASE_JWT, algorithms=["HS256"], audience="authenticated")
        auth_id = payload["sub"]
    except pyjwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = get_user_id_by_auth_id(auth_id)
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_id