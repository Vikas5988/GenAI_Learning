# Load environment variables from a .env file (e.g., GOOGLE_API_KEY)
from dotenv import load_dotenv
load_dotenv()

# Import necessary modules from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel


# 1. Initialize the LLM (Gemini 2.5 Flash Lite)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# 2. Output Parser: Extracts raw string content from the LLM's response message object
parser = StrOutputParser()

# 3. Define Prompt Templates
# First prompt: Instructs the model to act as a code generator
code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Code Generator"),
    ("human", "{topic}")
])

# Second prompt: Instructs the model to explain the generated code in simple terms
explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explain the code im Simple terms"),
    ("human", "Explain the following code in simple words: \n {code}")

])

# 4. First Chain (seq): Takes a topic, generates code, and parses the output to a string
seq = code_prompt | model | parser

# 5. Second Chain (seq2): Runs parallel processing on the incoming input (the generated code)
# - "code": Passes the generated code as-is using RunnablePassthrough()
# - "Explanation": Takes the generated code, passes it into explain_prompt, and calls the model
seq2 = RunnableParallel(
    {
        "code_print": RunnablePassthrough(),
        "Explanation": explain_prompt | model | parser
    }
)

# 6. Combined Chain: Pipes the output of 'seq' (generated code string) directly into 'seq2'
chain = seq | seq2

# 7. Execute the combined chain with the initial input topic
result = chain.invoke({"topic": "please write a code of palindrome in python "})

# 8. Print the resulting dictionary outputs
print(result['code_print'])
print(result['Explanation'])