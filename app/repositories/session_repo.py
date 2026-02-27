from app.db.mongodb import session_collection
from bson import ObjectId

async def create_session(data: dict):
    return await session_collection.insert_one(data)

async def get_session(session_id: str, user_id: str):
    return await session_collection.find_one({
        "_id": ObjectId(session_id),
        "user_id": user_id
    })

async def append_message(session_id: str, message: dict):
    return await session_collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$push": {"messages": message}}
    )

async def get_user_sessions(user_id: str):
    return session_collection.find({"user_id": user_id})

async def delete_session(session_id: str, user_id: str):
    return await session_collection.delete_one({
        "_id": ObjectId(session_id),
        "user_id": user_id
    })
