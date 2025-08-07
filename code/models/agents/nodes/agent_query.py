from typing import List, TypedDict
from langgraph.graph import StateGraph, START, END


from models.agents.nodes.node_embedding import embedding_query_node

from models.agents.nodes.node_retriever import retrieve_query_node
from models.agents.nodes.node_rerank import rerank_query_node
from models.agents.nodes.node_generate_answer import generate_answer_query_node
from models.agents.nodes.node_output import output_query_node

from utils.observability import start_trace
import utils.time as tiempo
from datetime import datetime


# Define state
class RAGState(TypedDict):
    query: str
    token: str

    embedding: List[float]
    documents: List[str]
    reranked_docs: List[str]
    
    response_RAG: str

    prompt: str
    answer_context: List[str]

    answer_final: dict


import logging
# **********************************************************************************
# Nodes for the RAG query graph
# **********************************************************************************
BEGIN = True
if BEGIN:
    datetime_now = str(datetime.now())
    # Auth Node # Verifica JWT y extrae user_id

    @tiempo.time_execution
    def auth_node(state: RAGState) -> RAGState:
        
        logger = logging.getLogger('/query')
        logger.info(f'buscando respuesta a pregunta -> {state["query"]}')
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo verificación Token de acceso", seed=datetime_now, output_text={"proc":"token"})

        state["token"] = "Token OK"
        # state["user_id"] = verify_token(state["token"])

        start_trace(user_id="crar", name="Interacción con el agente", input_text=state["token"], seed=datetime_now, output_text={"node": "auth_node", "proc":"token"})
        return state

    # Embedding Node
    @tiempo.time_execution
    def embed_node(state: RAGState) -> RAGState:
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Embedding Query ", seed=datetime_now, output_text={"node": "embed_node", "output": state["query"]})


        state["embedding"] = embedding_query_node(state["query"])

        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Embedding Query terminado", seed=datetime_now, output_text={"node": "embed_node", "output": state["embedding"]})
        return state

    # Retrieval Node
    @tiempo.time_execution
    def retrieve_node(state: RAGState) -> RAGState:
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Retrieve Query ", seed=datetime_now, output_text={"node": "retrieve_node", "output": state["query"]})

        state["documents"] = retrieve_query_node(state["query"], state["embedding"])

        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Retrieve Query terminado", seed=datetime_now, output_text={"node": "retrieve_node", "output": state["documents"]})
        return state

    
    # Rerank Node
    @tiempo.time_execution
    def rerank_node(state: RAGState) -> RAGState:
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Rerank Query ", seed=datetime_now, output_text={"node": "rerank_node", "output": state["query"]})

        state["reranked_docs"] = rerank_query_node(state["query"], state["documents"])

        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Rerank Query ", seed=datetime_now, output_text={"node": "rerank_node", "output": state["reranked_docs"]})
        return state

    # Generation Node
    @tiempo.time_execution
    def generateRAG_node(state: RAGState) -> RAGState:
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo generateRAG Query ", seed=datetime_now, output_text={"node": "generateRAG_node", "output": state["query"]})

        result = generate_answer_query_node(state["query"], state["reranked_docs"], state)

        state["prompt"] = result["prompt"]
        state["answer_context"] = result["answer_context"]


        state["response_RAG"] = result["answer_context"]

        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo generateRAG Query ", seed=datetime_now, output_text={"node": "generateRAG_node", "output": state["response_RAG"]})
        return state
    
    @tiempo.time_execution
    def output_node(state: RAGState):
        
        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Output Query ", seed=datetime_now, output_text={"node": "output_node", "output": state["query"]})

        state["answer_final"] = output_query_node(state["response_RAG"], state["reranked_docs"])

        start_trace(user_id="crar", name="Interacción con el agente", input_text="Nodo Output Query ", seed=datetime_now, output_text={"node": "output_node", "output": state["answer_final"]})

        logger = logging.getLogger('/query')
        logger.info(f'entrega de respuesta a pregunta -> {state["query"]}')
        return state
    
    # def response_node(state: RAGState):
    #     # sources = [{"page": c.get("page", 0), "text": c["text"]} for c in state["reranked_docs"]]
    #     return {
    #         "answer": state["answer"],
    #         "sources": sources
    #     }

    def validate_answer(state):
        answer = state["answer_final"]
        if len(answer) < 100:
            state["answer"] += "\n(Respuesta breve: el contenido web es limitado o irrelevante)"
        return state

    def stitch_responses(state):
        texts = state.get("retrieved_texts", [])
        state["answer"] = "\n---\n".join(texts[:3])  # une top 3 en una respuesta coherente
        return state

    # @observe(name="document_ingestion")
    # # Generation Node
    # def generate_node(state: RAGState) -> RAGState:
    #     state["answer"] = llm_generate(state["query"], state["reranked_docs"])
    #     return state

    # # Feedback Node
    # def feedback_node(state: RAGState) -> RAGState:
    #     trace = lf.trace(name="rag_query", input={"query": state["query"]})
    #     trace.span(name="retrieval", output={"docs": state["documents"]})
    #     trace.span(name="rerank", output={"docs": state["reranked_docs"]})
    #     trace.span(name="generation", output={"answer": state["answer"]})
    #     trace.end()
    #     return state

    # # Output Node
    # def output_node(state: RAGState) -> str:
    #     return state["answer"]


# **********************************************************************************
# **********************************************************************************



# **********************************************************************************
# Initialize the state graph
# **********************************************************************************
if BEGIN:

    graph = StateGraph(RAGState)

    graph.add_node("auth", auth_node)
    graph.add_node("embed", embed_node)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("rerank", rerank_node)
    graph.add_node("generateRAG", generateRAG_node)
    graph.add_node("output", output_node)

    # # graph.add_node("feedback", feedback_node)
    # # # graph.add_node("stitch", stitch_responses)
    # # # graph.add_node("validate", validate_answer)

    graph.set_entry_point("auth")
    graph.add_edge("auth", "embed")
    graph.add_edge("embed", "retrieve")
    graph.add_edge("retrieve", "rerank")
    graph.add_edge("rerank", "generateRAG")
    graph.add_edge("generateRAG", "output")

    graph.add_edge("output", END)

    # # graph.add_edge("retrieve", "stitch")
    # # graph.add_edge("stitch", "validate")
    # graph.add_edge("feedback", "output")
    


    # Compile the graph
    query_graph = graph.compile()


# **********************************************************************************
# **********************************************************************************
# **********************************************************************************



# from fastapi.testclient import TestClient
# from app import app

# client = TestClient(app)

# def test_health():
#     r = client.get("/health")
#     assert r.status_code == 200
#     assert r.json() == {"status": "ok"}

# def test_ingest():
#     r = client.post("/ingest", json={"urls": ["https://example.com"]})
#     assert r.status_code == 200
#     assert r.json()["status"] == "ingested"

# def test_question():
#     r = client.post("/question", json={"query": "¿Qué hace el sitio web?"})
#     assert r.status_code == 200
#     assert "answer" in r.json()