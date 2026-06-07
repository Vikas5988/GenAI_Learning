## NOT WORKING DUE TO API Connection and SSL Error

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()  # ← automatically finds .env in current or parent folder


model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

response = model.invoke("Who won IPL this year?")

print(response.content)