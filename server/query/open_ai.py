import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages=[
        {"role":"system", "content":"Answer the user query as detailed as possible in 300 tokens as the hard limit such that the response will not be cut-off"},
        {"role":"system", "content":"You are an expert in AI engineering"}
]

def get_ai_response():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    return completion.choices[0].message

if __name__ == "__main__":
    while(True):
        latest_query = messages[-1]
        print(latest_query["role"].upper() + ": " + latest_query["content"])

        query = input("USER: ")
        messages.append({"role":"user", "content":query})

        response = get_ai_response()
        messages.append(response)

def answer_query(context):
    template = f"Question: {context.get('query')}\nContext: {context.get('most_similar')}"
    
    messages=[
        {"role":"system", "content":"Answer the question using the context provided"},
        {"role":"user", "content":template}
    ]
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    
    return completion.choices[0].message

    
    

    
