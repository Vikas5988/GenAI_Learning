from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# 1.Prompt Template

prompt = ChatPromptTemplate.from_template(
    "Explain {TOPIC} in simple words "
)

# 2.Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# 3. Output Parser
parser = StrOutputParser()

chain = prompt|model|parser

response = chain.invoke("Devops Career Future")

print(response)
