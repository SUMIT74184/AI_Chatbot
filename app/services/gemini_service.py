import httpx
from app.core.config import settings

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-2.5-flash:generateContent"
)

async def generate_response(formatted_messages: list):
   
    payload = {
        "contents": formatted_messages,
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{GEMINI_URL}?key={settings.GEMINI_API_KEY}",
                json=payload
            )

        if response.status_code != 200:
            print(f"API Error: {response.status_code} - {response.text}")
            return "Temporary AI Issue. Please try again......"
        
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    
    except httpx.TimeoutException:
        return "AI response timed out. Try again in some time."
    
    except Exception as e:
        print(f"CRITICAL AI ERROR: {str(e)}")
        return "Unexpected AI Error occurred"