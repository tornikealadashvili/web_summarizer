import os                                 
from dotenv import load_dotenv             

load_dotenv(override=True)                 

BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")  # read setting, or use default value if not set
API_KEY = os.getenv("LLM_API_KEY", "ollama")                       # as ollama runs locally, it does not require an API key
MODEL = os.getenv("LLM_MODEL", "gemma3:4b")                        # model to use
MAX_CHARS = int(os.getenv("MAX_CHARS", "6000"))                   # maximum number of characters to summarize