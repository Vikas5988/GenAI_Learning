#import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # ← automatically finds .env in current or parent folder
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") /Not Required

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=.9,max_tokens=200) #WITH TOKEN LIMIT

messages=[]

print("---Welcome to the Chatbot---- Enter 0 to exit")
while True:
    prompt=input("You: ")
    if prompt == "0":
        break
    messages.append(prompt)
    response = model.invoke(messages)
    messages.append(response.content)
    print("Bot: ",response.content)