from fastapi import FastAPI
from app.ingest import ingest_documents
from app.query import answer_query

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ingest")
def ingest():
    
    return ingest_documents()
    # return {"message": "Ingest endpoint called"}

@app.post("/query")
def query(question: str):
    return answer_query(question)

# @app.get("/query")
# def query(payload: dict):
#     return answer_query(payload["question"])