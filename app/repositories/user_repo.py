from app.db.mongodb import users_collection
from bson import ObjectId

async def get_user_by_email(email:str):
    return await users_collection.find_one({"email":email})

async def create_user(user_data: dict):
    return await users_collection.insert_one(user_data)

async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})

async def delete_user(user_id: str):
    return await users_collection.delete_one({"_id": ObjectId(user_id)})
