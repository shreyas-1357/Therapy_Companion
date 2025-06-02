import os
from dotenv import load_dotenv

load_dotenv()

# Load configuration from environment variables
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
EMOTION_MODEL_URL = os.getenv("EMOTION_MODEL_URL")
LLM_MODEL_URL = os.getenv("LLM_MODEL_URL")

if not HUGGINGFACE_API_TOKEN:
    raise ValueError("HUGGINGFACE_API_TOKEN environment variable is not set")