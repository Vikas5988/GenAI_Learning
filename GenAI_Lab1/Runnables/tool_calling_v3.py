from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from rich import print


# Create a LangChain tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text."""
    return len(text)


# Create the Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# Give the LLM access to the tool
llm_with_tool = llm.bind_tools([get_text_length])

# Ask the LLM a question
result = llm_with_tool.invoke(
    "Return the number of characters in given text: "
    "Hello friends, Today we are learning LangChain tools"
)

#print(result)  # Inspect the raw AI response

# Check if the LLM requested a tool
if result.tool_calls:
    tool_call = result.tool_calls[0]

    # Get tool name and arguments
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    # Execute the requested tool
    tool_result = get_text_length.invoke(tool_args)

    # Send the tool result back to the LLM
    final_response = llm_with_tool.invoke(
        f"The length of the text is {tool_result}"
    )

    # Print the final response
    print(final_response)