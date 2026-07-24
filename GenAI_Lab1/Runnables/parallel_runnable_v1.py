from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# 1.Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# 2. Output Parser
parser = StrOutputParser()

# 3. Two different Prompts

short_promt = ChatPromptTemplate.from_template(
    "Explain {topic} in short"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

#topic = "AWS EC2"

chain = RunnableParallel({
    "short": short_promt|model|parser,
    "detailed": detailed_prompt|model|parser
})

result = chain.invoke({"topic":"AWS VPC"})

#result = chain.invoke(topic)  #If you want to use predefined topic

print(result['short'])
print("*" * 120)
print("*" * 120)
print(result['detailed'])