from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain import hub
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv
import os
import openai

## File is an attempt at using OpenAI and Langchain

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    openai.api_key = api_key
else:
    print("API key not found in .env file.")


# load documents
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/") # TEst website to read in as relevant data for questions

# split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1, chunk_overlap=0)
splits = text_splitter.split_documents(loader.load())

# embed and store splits
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()


rag_prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | rag_prompt | llm
rag_chain.invoke("What is Task Decomposition?") #Test question about loaded data

