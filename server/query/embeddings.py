import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-ada-002"

# TEST SCRIPT
# text = "Hello, world"
# response = openai.Embedding.create(input=text, model=EMBEDDING_MODEL)
# print(text, "\n")
# print(response['data'][0]['embedding'])

def get_embedding(text: str):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']
