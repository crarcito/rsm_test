from fastapi import APIRouter

# from ..schemas import QueryRequest
from models.query import Query
from models.ingest import Ingestion


api_router = APIRouter()

@api_router.get("/health")
async def health():
    return {"status": "200 OK"}

@api_router.post("/ingest")
async def ingest():
    results = Ingestion.add_ingest_urls()
    
    return {"status": results}
    # return {"message": "ingested successfully"}

# @api_router.post("/query" , response_model=QueryResponse)
@api_router.post("/query")
async def query(req: str):
    # results = Query.get_question_answer(namecollection="test_collection", question=req.query, matching_count=req.top_k)

    results = Query.get_question_answer(question=req, matching_count=2)

    # return {"results": results}return "shao"
    # return {"results": results}

    return {
            "answer": results,
            "sources": [
                    { "page": 1, "text": "<passage text>" },
                    ]
            }

    # return results