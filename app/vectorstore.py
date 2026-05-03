from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)


def save_vectorstore(vs, path="faiss_index"):
    vs.save_local(path)


def load_vectorstore(path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)