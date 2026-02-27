import httpx
from app.core.config import Settings

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-pro:generateContent"
)


async def generate_response(messages: list):
    
    payload = {
        "content":messages,
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{GEMINI_URL}?key={Settings.GEMINI_API_KEY}",
                json=payload
            )

        if response.status_code != 200:
            return "Temporary AI Issue. PLease try again......"
        
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    
    except httpx.TimeoutException:
        return "AI response timed out. Try again in some times"
    
    
    except Exception:
        return "Unexpected AI Error occurred"