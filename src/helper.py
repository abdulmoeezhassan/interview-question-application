from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from src.prompt import *


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


def file_processing(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    question_gen=""

    for page in data:
     question_gen+=page.page_content

    splitter_ques_gen = TokenTextSplitter(
    chunk_size=10000,
    chunk_overlap=200
)
    chunk_ques_gen=splitter_ques_gen.split_text(question_gen)
    document_ques_gen=[Document(page_content=t) for t in chunk_ques_gen]
    splitter_ques_gen = TokenTextSplitter(
    chunk_size=10000,
    chunk_overlap=200
)
    chat = ChatGroq(temperature=0.3, 
                model_name="llama-3.3-70b-versatile")
