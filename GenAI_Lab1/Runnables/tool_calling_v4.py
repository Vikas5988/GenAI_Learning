from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print
#1 creating a tool 
@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)


# Store tools in a dictionary for easy lookup
tools = {
    "get_text_length" : get_text_length
}

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Bind the defined tools to the LLM
llm_with_tool = llm.bind_tools([get_text_length])

# Initialize conversation history
message = []
prompt = input("You: ")
# Convert user input to LangChain message format and add to conversation history
query = HumanMessage(prompt)
message.append(query)

# Send user message to LLM and get response
result = llm_with_tool.invoke(message)

# Add LLM response to conversation history
message.append(result)

# Check if LLM decided to call a tool
if result.tool_calls:
    # Extract the tool name from LLM's decision
    tool_name = result.tool_calls[0]["name"]
    # Execute the tool with the parameters provided by LLM
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    # Add tool result to conversation history
    message.append(tool_message)

# Send conversation history back to LLM for final response
result = llm_with_tool.invoke(message)

# Print the final response from LLM
print(result)
# print(result.content)