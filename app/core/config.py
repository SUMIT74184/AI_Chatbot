from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GEMINI_API_KEY:str
    GEMINI_API_SECRET:str
    GEMINI_API_URL:str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

Settings = Settings()        
    