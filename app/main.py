from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from app.vectorstore import load_vectorstore
from app.rag_pipeline import run_rag
from app.auth import authenticate

app = FastAPI()

vectorstore = load_vectorstore()


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(req: QueryRequest, authorization: str = Header(None)):
    if not authenticate(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized")

    answer = run_rag(vectorstore, req.question)

    return {"answer": answer}