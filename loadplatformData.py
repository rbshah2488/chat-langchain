import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import uuid
import ingest

WEAVIATE_URL = os.environ["WEAVIATE_URL"]
WEAVIATE_API_KEY = os.environ["WEAVIATE_API_KEY"]
RECORD_MANAGER_DB_URL = os.environ["RECORD_MANAGER_DB_URL"]

def load_platform_docs():
    print("inside load_platform_docs")
    documents = load_documents_from_files()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    docs_transformed = text_splitter.split_documents(
        documents
    )
    print(f"docs_transformed: {docs_transformed}")
    ingest.ingest_docs_helper(docs_transformed)
    

def load_documents_from_files():
    txt_files = ["./data/someTestDoc.txt"]
    txt_loaders = [TextLoader(file_name) for file_name in txt_files]
    documents = []
    for loader in txt_loaders:
       documents.extend(loader.load())
    return documents

load_platform_docs()