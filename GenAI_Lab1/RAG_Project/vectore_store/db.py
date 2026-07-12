from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

EMBED1="gemini-embedding-001"
EMBED2= "gemini-embedding-2-preview"
EMBED3= "gemini-embedding-2"

embedding_model = GoogleGenerativeAIEmbeddings(model=EMBED3)

vectorstore1 = Chroma.from_documents(
    documents = docs,
    embedding= embedding_model,
    persist_directory= "chroma-db"
)

result = vectorstore1.similarity_search("what is used for data analysis?",k=3)


for r in result:
    print(r.page_content)
    print(r.metadata)
    

retriver = vectorstore1.as_retriever() #Convert the vector store into a standardized "Retriever" interface

docs = retriver.invoke("Explain deep learning")  #Query the retriever with a natural language string. 

for d in docs:
    print(d.page_content)