#import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # ← automatically finds .env in current or parent folder

#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") /Not Required

#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=.9,max_token=200) #WITH TOKEN LIMIT

response = model.invoke("Who are Agentic AI")

print(response.content)