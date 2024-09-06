import os
from langchain_community.llms import GPT4All

def get_llm():
    """
    Initialize and return the GPT4All language model with parameters from environment variables.
    """
    # Get the model path and context size from environment variables, with default values
    model_path = os.getenv('MODEL_PATH', 'models/ggml-gpt4all-j-v1.3-groovy.bin')
    model_n_ctx = int(os.getenv('MODEL_N_CTX', '2048'))

    # Initialize the GPT4All model
    try:
        llm = GPT4All(model=model_path, max_tokens=model_n_ctx)
    except TypeError as e:
        print(f"Error initializing model: {e}")
        raise
    
    return llm
