from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv() 

embeddings1 = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector1 = embeddings1.embed_query("hello, world!")
print("Default embedding dimesions: ", len(vector1))

embeddings2 = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",output_dimensionality=600)
vector2 = embeddings2.embed_query("hello, world!")

#print(vector2)
print("Dimesion set to 600 : ", len(vector2))