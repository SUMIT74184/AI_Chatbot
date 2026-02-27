import time
from collections import defaultdict
from fastapi import HTTPException

rate_limit_store = defaultdict(list)
REQ_LIMIT = 5
WINDOW_SECONDS = 60 

def check_rate_limit(user_id:str):
    now = time.time()
    requests = rate_limit_store[user_id]
    
    rate_limit_store[user_id]=[
        rq for rq in requests if now - rq < WINDOW_SECONDS
    ]
    
    if len(rate_limit_store[user_id]) >= REQ_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    rate_limit_store[user_id].append(now)
