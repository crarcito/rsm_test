from fastapi import FastAPI
from config import config

from langfuse._client.client import Langfuse
from pydantic import BaseModel


from app.ingest import ingest_urls

app = FastAPI()

settings = config['development']
LANGFUSE_SECRET_KEY = settings.LANGFUSE_SECRET_KEY
LANGFUSE_PUBLIC_KEY = settings.LANGFUSE_PUBLIC_KEY
LANGFUSE_HOST = settings.LANGFUSE_HOST

URL_1 = settings.URL_1
URL_2 = settings.URL_2  


langfuse = Langfuse(
    public_key=LANGFUSE_PUBLIC_KEY,
    secret_key=LANGFUSE_SECRET_KEY,
    host=LANGFUSE_HOST
    )   



@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest")
def ingest():
    urls = [URL_1, URL_2]
    status_ingest = ingest_urls(urls)
    return(status_ingest)

    # return {"status": "ingested", "count": len(urls)}

# @app.post("/ingest")
# def ingest():
    
#     return ingest_documents()
#     # return {"message": "Ingest endpoint called"}

# @app.post("/query")
# def query(question: str):
#     return answer_query(question)

# @app.get("/query")
# def query(payload: dict):
#     return answer_query(payload["question"])