from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

data=TextLoader("RAG_Project/Document_Loader/RHEL_Concept.txt",encoding="utf-8")
docs=data.load()

template = ChatPromptTemplate.from_messages([
    "System","You are an AI Assitance who summarizes the in simple and easy language",
    "Human","{data}"
])

prompt=template.format(data=docs[0].page_content)

result=model.invoke(prompt)
print(result.content)