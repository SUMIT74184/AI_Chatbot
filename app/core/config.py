from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GEMINI_API_KEY:str
    GEMINI_API_SECRET:str
    GEMINI_API_URL:str
    GEMINI_API_SECRET: Optional[str] = None
    GEMINI_API_URL: Optional[str] = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()        
    