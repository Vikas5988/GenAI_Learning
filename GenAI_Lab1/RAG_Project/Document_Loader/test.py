from langchain_community.document_loaders import TextLoader

data=TextLoader("Document_Loader/RHEL_Concept.txt",encoding="utf-8")

docs=data.load()

#print(docs)

print(len(docs))


# print("*" * 100)
# print(docs[0])

# print("*" * 100)
# print(docs[0].page_content)