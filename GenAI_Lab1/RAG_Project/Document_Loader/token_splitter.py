from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

Splitter = TokenTextSplitter(
    chunk_size = 200,
    chunk_overlap = 5
)

data=PyPDFLoader("Document_Loader/aws_lambda_guide.pdf")

docs=data.load()

chunks = Splitter.split_documents(docs)

print(len(chunks))

print(chunks[6].page_content)





