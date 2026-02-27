from pydantic import BaseModel,Field

class CreateSessionRequest(BaseModel):
    title: str = Field(min_length=1,max_length=300)
    

class CreateSessionResponse(BaseModel):
    session_id: str
    title: str