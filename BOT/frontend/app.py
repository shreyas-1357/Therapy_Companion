import streamlit as st
import requests
from streamlit_chat import message

# Page config
st.set_page_config(page_title="🧠 Therapy Companion Bot", page_icon="💬", layout="wide")

# Custom CSS for better visuals
st.markdown("""
    <style>
    .block-container {
        padding: 2rem 4rem;
        background-color: #f5f7fa;
    }
    .stChatMessage.user {
        background-color: #dcf8c6;
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
        font-size: 16px;
    }
    .stChatMessage.bot {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1>🧠 Therapy Companion Bot</h1>
        <p style='font-size: 18px; color: #555;'>A caring, intelligent companion for your mental wellness journey</p>
    </div>
""", unsafe_allow_html=True)

# Chat state
user_id = 1
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
input_text = st.chat_input("Share your thoughts or feelings...")

if input_text:
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://localhost:8000/chat",
            json={"user_id": user_id, "message": input_text}
        ).json()

        st.session_state.chat_history.append(("user", input_text))
        st.session_state.chat_history.append(("assistant", response["reply"]))

        st.success(f"🧠 Emotion Detected: {response['emotion'].capitalize()}")

# ...existing code...

# Display chat messages
for i, (role, msg) in enumerate(st.session_state.chat_history):
    is_user = role == "user"
    message(msg, is_user=is_user, key=f"msg_{i}")
