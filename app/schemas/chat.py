from pydantic import BaseModel,Field

class MessageRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)

class ChatResponse(BaseModel):
    session_id: str
    user_message: str
    assistant_response: str