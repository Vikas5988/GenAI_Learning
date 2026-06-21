from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = ChatPromptTemplate.from_messages([
    "system",
        """You are an expert data extraction assistant. Your task is to extract key information from the provided paragraph about a movie and format it into a clean, structured list.

Extract the following details:
- Movie Title:
- Release Year:
- Director:
- Main Cast:
- Setting/Era:
- Core Themes:
- Box Office/Critical Reception:
- IMDb Rating:
- Key Highlights/Awards:

If a specific detail is not mentioned in the text, mark it as 'Not specified'.""",
"human", "Extract Information from this paragrah: {paragraph}"
            
]
)

para = input("Enter the Movie raw data: ")

final_prompt = prompt.invoke({"paragraph":para})

response=model.invoke(final_prompt)

print(response.content)
