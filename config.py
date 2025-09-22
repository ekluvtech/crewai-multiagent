import os


#ollama
OLLAMA_URL= os.getenv('OLLAMA_URL','http://localhost:11434')
LLM_MODEL = os.getenv('LLM_MODEL','ollama/llama3.2')
EMBED_MODEL = os.getenv('EMBED_MODEL','mxbai-embed-large:latest')
