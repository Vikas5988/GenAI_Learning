# PDF Loader with Token based Splitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


template = ChatPromptTemplate.from_messages([
    "System","You are an AI Assitance who summarizes the in simple and easy language",
    "Human","{data}"
])



result=model.invoke(prompt)
print(result.content)