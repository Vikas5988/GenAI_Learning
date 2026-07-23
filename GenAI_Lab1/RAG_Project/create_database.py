#Step1 : Load PDF
#Step2 :Split into chunk
#Step3 :Create the embeddings
#Step4 :Store into Chroma DB

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

data=PyPDFLoader("Document_Loader/aws_lambda_guide.pdf")
docs=data.load()

Splitter = RecursiveCharacterTextSplitter(
    chunk_size = 600,
    chunk_overlap = 100
)

chunks = Splitter.split_documents(docs)

EMBED1="gemini-embedding-001"
EMBED2= "gemini-embedding-2-preview"
EMBED3= "gemini-embedding-2"

embedding_model = GoogleGenerativeAIEmbeddings(model=EMBED3)

vectore_store = Chroma.from_documents(
    documents = chunks,
    embedding = embedding_model,
    persist_directory= "chroma-db-main"
    )


