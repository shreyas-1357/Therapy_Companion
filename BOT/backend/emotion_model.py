import requests
from backend.config import HUGGINGFACE_API_TOKEN, EMOTION_MODEL_URL

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def detect_emotion(text):
    payload = {"inputs": text}
    response = requests.post(EMOTION_MODEL_URL, headers=headers, json=payload)
    try:
        predictions = response.json()[0]
        top_emotion = max(predictions, key=lambda x: x["score"])
        return top_emotion["label"]
    except Exception as e:
        print("Emotion detection failed:", e)
        return "neutral"