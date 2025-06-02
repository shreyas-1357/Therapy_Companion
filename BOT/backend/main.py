from fastapi import FastAPI
from pydantic import BaseModel
from backend.emotion_model import detect_emotion
from backend.llm_response import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: int
    message: str

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    emotion = detect_emotion(req.message)
    context = "No past memory yet."
    response = generate_response(context, emotion, req.message)

    return {
        "reply": response,
        "emotion": emotion
    }