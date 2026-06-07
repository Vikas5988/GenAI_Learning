from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()  # ← automatically finds .env in current or parent folder

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

print(model)

response = model.invoke("Why do we work?")

print(response.content)