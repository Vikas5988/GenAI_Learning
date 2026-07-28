from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from rich import print 

#1 creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

llm_with_tool=llm.bind_tools([get_text_length])

result = llm.invoke("Return the number of character in given text: Hello friends, Today we are learning Langchain tools")

result2 = llm_with_tool.invoke("Return the number of character in given text: Hell friends, Today we are learning Langchain tools")

print("Output from  LLM Only : ",result)
print("*"*50)
print("*"*50)

print("Output from LLM with Tools binding : ",result2)
