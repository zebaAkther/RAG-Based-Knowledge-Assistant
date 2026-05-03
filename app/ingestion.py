import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import CHUNK_SIZE, CHUNK_OVERLAP


def load_documents(folder_path="documents"):
    docs = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            docs.append(text)

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())

    return docs


def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []
    for doc in docs:
        chunks.extend(splitter.split_text(doc))

    return chunks