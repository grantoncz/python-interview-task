import os
from dotenv import load_dotenv
load_dotenv()

# load open ai key from env
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
