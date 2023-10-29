from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")
COLLECTION_NAME = 'state_of_union_vectors'

loader = TextLoader('state_of_the_union.txt', encoding='utf-8')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query('Testing the model')
doc_vectors = embeddings.embed_documents([t.page_content for t in texts[:5]])

db = PGVector.from_documents(embedding=embeddings, documents=texts, collection_name=COLLECTION_NAME,
              connection_string=CONNECTION_STRING)

query = input("QUESTION: ")

similar = db.similarity_search_with_score(query, k=2)
similar_text = ""

for doc in similar:
    similar_text += doc[0].page_content

template = """Answer the question using the context provided.
Question: {question}
Context: {context} """

prompt = PromptTemplate(template=template, input_variables=["question","context"])

llm = openai.OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

answer = llm_chain.run({'question': query,'context':similar_text})

answer_template = f"\nCONTEXT:\n{similar_text}\n\nANSWER:{answer}"
print(answer_template)
