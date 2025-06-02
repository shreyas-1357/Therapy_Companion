import requests
import logging
from backend.config import HUGGINGFACE_API_TOKEN, LLM_MODEL_URL

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_response(context, emotion, user_input):
    prompt = f"""
You are a compassionate therapy assistant. Your job is to help users reflect on their feelings and support their emotional well-being.

Context: {context}
Detected Emotion: {emotion}
User: {user_input}

Therapist:"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(LLM_MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        result = response.json()
        if not result or not isinstance(result, list) or len(result) == 0:
            logger.error(f"Unexpected API response format: {result}")
            return "I apologize, but I'm having trouble processing your request right now."
            
        return result[0]["generated_text"].strip()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        return "I'm experiencing connection issues. Please try again in a moment."
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return "I'm here for you. Please share more if you'd like."