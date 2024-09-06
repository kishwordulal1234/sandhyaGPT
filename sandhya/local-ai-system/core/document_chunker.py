from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

chunk_size = 500
chunk_overlap = 50

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)
