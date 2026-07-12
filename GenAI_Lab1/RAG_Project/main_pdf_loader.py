from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

data=PyPDFLoader("Document_Loader/aws_lambda_guide.pdf")

docs=data.load()

template = ChatPromptTemplate.from_messages([
    "System","You are an AI Assitance who summarizes the in simple and easy language",
    "Human","{data}"
])

#prompt=template.format(data=docs[1].page_content)
prompt=template.format(data=docs)

result=model.invoke(prompt)
print(result.content)