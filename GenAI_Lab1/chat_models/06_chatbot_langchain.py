#import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()  # ← automatically finds .env in current or parent folder
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") /Not Required

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=.9,max_tokens=200) #WITH TOKEN LIMIT

messages=[
    SystemMessage(content = "You are an expert in Devops and AI ")
]

print("---Welcome to the Chatbot---- Enter 0 to exit")
while True:
    prompt=input("You: ")
    if prompt == "0":
        break
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ",response.content)