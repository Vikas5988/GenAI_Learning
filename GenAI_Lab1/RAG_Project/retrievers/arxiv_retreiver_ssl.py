# Disable SSL Verification to run from Office Laptop

import requests
requests.packages.urllib3.disable_warnings()
original_request = requests.Session.request
def patched_request(self, method, url, **kwargs):
    kwargs['verify'] = False
    return original_request(self, method, url, **kwargs)
requests.Session.request = patched_request

from langchain_community.retrievers import ArxivRetriever

# create the retriever
retriever = ArxivRetriever(
    load_max_docs=4,
    top_k_results=4,  #Default value is 3, so default results will be 3 if not set
    load_all_available_meta=True
)

# query arxiv
docs = retriever.invoke("Devops Career")

# print results
for i, doc in enumerate(docs):
    print(f"\nResult {i+1}")
    print("Title:", doc.metadata.get("Title"))
    print("Authors:", doc.metadata.get("Authors"))
    print("Summary:", doc.page_content)  # print first 500 characters