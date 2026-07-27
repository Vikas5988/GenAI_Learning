from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

search_tool = TavilySearchResults(max_result=5)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant.
        Summarize the below news into clear bullet points
    
        {news}
    """
)

chain = prompt | model | parser

news_result = search_tool.run("Latest news about Cricket series by India")

print(news_result)
result = chain.invoke({"news": news_result})

print(result)


print(search_tool.description)
print(search_tool.name)
print(search_tool.args)