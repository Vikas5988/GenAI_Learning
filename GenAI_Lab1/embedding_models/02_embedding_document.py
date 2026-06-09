from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv() 

EMBED1="gemini-embedding-001"
EMBED2= "gemini-embedding-2-preview"
EMBED3= "models/gemini-embedding-2"

text=[" This is",
    "a sample text for embedding",
     "for testing purpose and experiment"
]

print(type(text))
embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBED3,
        output_dimensionality=64
        )
vector= embeddings.embed_documents(text)

print(vector)

print(len(vector[1]))



