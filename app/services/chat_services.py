from app.db.mongodb import session_collection
from app.services.gemini_service import generate_response
from datetime import datetime
from bson import ObjectId
# from app.repositories.session_repo import get_session,append_message


async def send_message(session_id:str,user_id:str,message:str):
    session = await session_collection.find_one({
        "_id":ObjectId(session_id),
        "user_id":user_id
    })
    
    if not session:
        return None
    
    user_msg={
        "role":"user",
        "content":message,
        "timestamp":datetime.utcnow() 
    }
    
    await session_collection.update_one(
        {"id":ObjectId(session_id)},
        {"$push":{"messages":user_msg}}
    )
    
    updated = await session_collection.find_one(
        {"_id":ObjectId(session_id)}
    )
    
    last_message = updated["messages"][-15:]
    
    gemini_format = []
    for msg in last_message:
        role = "user" if msg["role"] == "user" else "model"
        gemini_format.append({
            "role":role,
            "parts":[{"text": msg["context"]}]
        })
        
    ai_reply= await generate_response(gemini_format)
    
    assistant_msg={
    "role":"assistant",
    "content":ai_reply,
    "timestamp": datetime.utcnow()
    }
    
    await session_collection.update_one(
        {"_id":ObjectId(session_id)},
        {"$push":{"message":assistant_msg}}
    )
    
    return ai_reply