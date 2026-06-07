from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import httpx
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

load_dotenv()

disable_client = httpx.Client(verify=False)

llm = HuggingFaceEndpoint(
    repo_id="nvidia/Gemma-4-31B-IT-NVFP4",
#    temperature=0.7,
#    max_length=1024,
#    client=disable_client
)
model = ChatHuggingFace(llm=llm)

response = model.invoke(" Does Devops is good career in today AI Era")

print(response.content)