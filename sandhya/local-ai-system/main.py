from core.ai_engine import get_llm
from core.document_chunker import split_documents
from terminal.processor import process_documents

def main():
    llm = get_llm()
    # Your code to interact with the LLM

    documents = process_documents()
    chunks = split_documents(documents)
    # Your code to use chunks with LLM

if __name__ == "__main__":
    main()
