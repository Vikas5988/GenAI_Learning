
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

#load an existing Chroma vector database from your local storage
vectorstore = Chroma(
    persist_directory ="chroma-db-main",
    embedding_function = embedding_model   #Provides the database with the exact same AI model used to create it in the first place
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,     # k = number of final documents to return to the user/LLM
        "fetch_k":10,  # number of candidate documents to initially fetch from the vector store before applying MMR re-ranking
        "lambda_mult":0.5  #controls the relevance vs diversity trade-off (range 0 to 1)
        }
)

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

prompt = ChatPromptTemplate.from_messages([
    ("system","""You are an helpful AI Assitance.
            Use ONLY the provided context to answer the question.
            If the answer is not present in the context, say: "I could not find the answer in the document."""),
        
    ("human","""Context: {context}  Question: {question}""")
])

print("RAG System Created")
print("Press 0 to exit")

while True:
    query = input("You: ")
    if query == "0":
        break
    
    docs = retriever.invoke(query)
    
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)
    
    print(f"\n AI: {response.content}")

