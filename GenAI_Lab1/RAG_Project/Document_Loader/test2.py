#PDF Document Loader

from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("Document_Loader/aws_lambda_guide.pdf")

docs=data.load()

print(len(docs))

#print(docs)

print(docs[0].page_content)

print(docs[4].page_content)

