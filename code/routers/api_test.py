from fastapi import APIRouter

# # from ..schemas import QueryRequest
from models.query import Query
from models.ingest import Ingestion

from agents.query_graph import rsm_graph

from config import config
config_env = config['default']


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
async def query(question: str):

    # return prueba.invoke({"customer_name": question})

    # return prueba.invoke({"query": question})

    #     state = {"my_var": "", "customer_name": "", "query": ""}

    state_graph = rsm_graph.invoke(
        {
            "query": question,
            "token": config_env.SECRET_KEY_APP,      
            "embedding": [],
            "documents": [""],
            "answer": ""
        }
    )
    return state_graph
        
# "embedding": [],

    # results = Query.get_question_answer(question=question, matching_count=2)
    # return results

