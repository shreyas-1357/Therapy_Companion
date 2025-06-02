# 🧠 Emotion-Aware Therapy Companion Bot

An intelligent mental wellness assistant powered by Hugging Face LLMs and emotional memory. This bot adapts to your emotions, remembers past conversations, and supports mental wellness through context-aware interactions.

> 🔗 GitHub: [shreyas-1357/Therapy_Companion](https://github.com/shreyas-1357/Therapy_Companion)

---

## 🚀 Features

- 💬 Natural conversations using Hugging Face language models.
- 🧠 Real-time emotion detection from user input.
- 📚 Context and mood-aware memory using vector storage.
- 🖥️ ChatGPT-style frontend with `streamlit-chat`.
- 🗃️ Persistent journaling with MySQL backend.

---

## 📦 Tech Stack

- **Frontend**: Streamlit + `streamlit-chat`
- **Backend**: Python + FastAPI
- **AI Models**: Hugging Face Transformers (LLMs & emotion classifier)
- **Database**: MySQL
- **APIs**: Hugging Face Inference API

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/shreyas-1357/Therapy_Companion.git
cd Therapy_Companion
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Hugging Face API Key
Create a .env file in the root directory:

ini
Copy
Edit
HUGGINGFACE_API_KEY=your_huggingface_token
👉 Get your token here: https://huggingface.co/settings/tokens

4. Set Up MySQL
Create a database named therapy_bot in MySQL.

Update the connection string in backend/database.py:

python
Copy
Edit
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/therapy_bot"
Then run:

bash
Copy
Edit
python backend/create_tables.py
▶️ Running the Project
Run Backend (FastAPI)
bash
Copy
Edit
cd backend
uvicorn main:app --reload
Run Frontend (Streamlit)
Open a new terminal:

bash
Copy
Edit
cd frontend
streamlit run app.py
📸 Screenshots (Coming Soon)
Stay tuned for UI previews!

✅ To-Do
 Add user login and session management

 Integrate journaling insights/analytics

 Improve model response handling

 Add voice/chat history export

📄 License
This project is licensed under the AVCOE License.

🙌 Acknowledgements
Hugging Face Transformers

Streamlit

MySQL

Uvicorn & FastAPI

👨‍💻 Author
Made with ❤️ by Shreyas

python
Copy
Edit

Let me know if you'd like to:
- embed GIFs or screenshots
- prepare a version for Hugging Face Spaces
- include Docker support  
I'm happy to help polish this further!
