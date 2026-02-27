
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import Settings

client = AsyncIOMotorClient(Settings.MONGO_URI)
db = client[Settings.DB_NAME]

users_collection = db["users"]
session_collection = db["sessions"]


