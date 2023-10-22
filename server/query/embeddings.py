import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

text = "Hello, world"
response = openai.Embedding.create(input=text, model="text-embedding-ada-002")

print(text, "\n")
print(response['data'][0]['embedding'])
