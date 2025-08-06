from fastapi import APIRouter, HTTPException
from utils.observability import start_trace, log_span, log_error, CrearArchivoLog
from datetime import datetime
# # from ..schemas import QueryRequest
from models.query import Query
from models.ingest import Ingestion



from models.agents.nodes.agent_query import query_graph


from config import config
config_env = config['default']


api_router = APIRouter()
# setup_observability(api_router)

@api_router.get("/health")
async def health():
    return {"status": "200 OK"}

@api_router.post("/ingest")
async def ingest():
    results = Ingestion.add_ingest_urls()
    
    return {"status": results}
    # return {"message": "ingested successfully"}


# @api_router.post("/query" , response_model=QueryResponse)

import logging

@api_router.post("/query")
async def query(question: str):
    trace = start_trace(user_id="crar", name="start query", input_text=question, seed=str(datetime.now()), output_text=dict())

    try:
        CrearArchivoLog()
        logger = logging.getLogger('test_rsm')
        logger.info(f'iniciando query - {question}')

        state_graph = query_graph.invoke(
            {
                "query": question,
                "token": config_env.SECRET_KEY_APP,

                "embedding": [],
                "documents": [""],
                "reranked_docs": [""],
                
                "response_RAG": "",

                "prompt": "",
                "answer_context": [""],

                "answer_final": dict()
            }
        )

        logger.info(f'saliendo de query - {question}')

        # log_span(trace, name="endpoint_query", input_data={"query": question}, output_data=state_graph["answer_final"])
        trace = start_trace(user_id="crar", name="end query", input_text=question, seed=str(datetime.now()), output_text=state_graph["answer_final"])

        return state_graph["answer_final"]
        
    except Exception as e:
        # log_error(trace, str(e))
        logger.info(f'error en responder - {e.args}')
        trace = start_trace(user_id="crar", name="Error LLM inference calls", input_text=question,  seed=str(datetime.now()), 
                            output_text={
                                        "answer": state_graph["answer_context"],
                                        "error": e.args
                                    }
                            )
        return {
                    "answer": question,
                    "error": [{"page": 0, "text":  HTTPException(status_code=500, detail="Error en la consulta semántica")}]
                }
