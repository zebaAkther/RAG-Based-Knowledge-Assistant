from app.ingestion import load_documents, chunk_documents
from app.vectorstore import create_vectorstore, save_vectorstore

docs = load_documents("documents")
chunks = chunk_documents(docs)

vs = create_vectorstore(chunks)
save_vectorstore(vs)

print("Vector DB created!")