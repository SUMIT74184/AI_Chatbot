from app.repositories import user_repo
from app.core.security import hash_password, verify_password
from app.core.security import create_access_token
from datetime import datetime

async def register_user(email:str, password:str):
    existing =await user_repo.get_user_by_email(email)
    if existing:
        return None
    
    user = {
        "email":email,
        "password":hash_password(password),
        "created_at":datetime.utcnow()
    }
    result = await user_repo.create_user(user)
    return str(result.inserted_id)

async def authenticate_user(email:str, password:str):
    user = await user_repo.get_user_by_email(email)
    if not user:
        return None
    
    if not verify_password(password, user["password"]):
        return None
    
    token = create_access_token({"sub":str(user["_id"])})
    return token