from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.schemas.chat import ChatResponse, MessageRequest
from app.services import auth_Service, chat_services
from app.services.auth_Service import register_user, authenticate_user
from app.services.chat_services import send_message
from app.core.security import verify_token
from app.schemas.session import CreateSessionRequest
from app.repositories import session_repo
from datetime import datetime
from app.core.ratelimit import check_rate_limit

router =APIRouter()
security = HTTPBearer()

async def get_current_user(
    credentials:HTTPAuthorizationCredentials = Depends(security)
):
    payload = verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid_token")
    return payload["sub"]


@router.post("/auth/register")
async def register(email:str, password:str):
    user_id = await register_user(email,password)
    if not user_id:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message":"Registered successfully"}

@router.post("/auth/login")
async def login(email:str, password:str):
    token = await authenticate_user(email,password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token":token, "token_type":"bearer"}


# Creating the Session

@router.post("/sessions")
async def create_session(
    request: CreateSessionRequest,
    user_id:str = Depends(get_current_user)
):
    session = {
        "user_id": user_id,
        "title": request.title,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "messages":[]
    }
    
    result= await session_repo.create_session(session)
    
    return {
        "id":str(result.inserted_id),
        "title":request.title
    }

    # first message 

@router.post("/chat/{session_id}", response_model=ChatResponse)
async def chat(
    session_id: str,
    request: MessageRequest,
    user_id: str = Depends(get_current_user)
):
    check_rate_limit(user_id)

    reply = await send_message(
        session_id,
        user_id,
        request.message
    )

    if not reply:
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "session_id": session_id,
        "user_message": request.message,
        "assistant_response": reply
    }

    
# Get All the sessions

@router.get("/sessions")
async def get_sessions(user_id: str = Depends(get_current_user)):
    sessions=[]
    cur = await session_repo.get_user_sessions(user_id)
    
    async for s in cur:
        sessions.append({
            "id":str(s["_id"]),
            "title":s["title"]
        })
    
    return sessions


# Get Session By ID
@router.get("/sessions/{session_id}")
async def get_session(
    session_id:str,
    user_id:str = Depends(get_current_user)
    
):
    session = await session_repo.get_session(session_id, user_id)
    
    if not session:
        raise HTTPException(status_code=404,detail="Session not found")
    
    session["id"] = str(session["_id"])
    del session["_id"]
        
    return session


# Delete Session by Id
@router.delete("/sessions/{session_id}")
async def delete_session(
    session_id:str,
    user_id:str = Depends(get_current_user)
):
    result = await session_repo.delete_session(session_id, user_id)

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {"message":"session deleted successfully"}

# Delete User by Id
@router.delete("/users")
async def delete_user_route(user_id: str = Depends(get_current_user)):
    if not await auth_Service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}





























