from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from typing import List,Optional

from dotenv import load_dotenv
load_dotenv()

class Movie(BaseModel):
    Title:str
    Release_year:Optional[int]
    Genre: List[str]
    Director: Optional[str]
    Cast: List[str]
    IMDB_Rating:Optional[float]
    Summary:str
  
parser = PydanticOutputParser(pydantic_object=Movie)  

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = ChatPromptTemplate.from_messages([
    ("system","""
    Extract Movie Information from the paragraph
    {format_instructions}
    """     ),
     ("human","{paragraph}" )   
]
)

para = input("Enter the Movie raw data: ")

final_prompt = prompt.invoke({
    "paragraph":para,
    'format_instructions': parser.get_format_instructions()
    })

response=model.invoke(final_prompt)

print(response.content)

movie_data_cleaned = parser.parse(response.content)
