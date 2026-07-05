from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

Splitter = CharacterTextSplitter(
    separator="",      # To override the default /n/n separator
    chunk_size = 10,
    chunk_overlap = 2
)

data=TextLoader("Document_Loader/notes.txt")

docs=data.load()

chunks= Splitter.split_documents(docs)

print(len(chunks))

print(chunks)

for i in chunks:
    print(i.page_content)
    print("*******")
    print("******")