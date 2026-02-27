from fastapi import FastAPI
from app.api.routes import router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request

app = FastAPI(title="AI Chatbot Backend")

app.include_router(router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid input", "errors": exc.errors()}
    )
