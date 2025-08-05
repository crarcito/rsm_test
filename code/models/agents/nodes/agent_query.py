from typing import List, TypedDict


from langgraph.graph import StateGraph, START, END

from models.agents.nodes.node_embedding import embedding_query_node

from models.agents.nodes.node_retriever import retrieve_query_node
from models.agents.nodes.node_rerank import rerank_query_node
from models.agents.nodes.node_generate_answer import generate_answer_query_node
from models.agents.nodes.node_output import output_query_node


# lf = Langfuse(public_key="...", secret_key="...")

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



# **********************************************************************************
# Nodes for the RAG query graph
# **********************************************************************************
BEGIN = True
if BEGIN:
    # Auth Node
    def auth_node(state: RAGState) -> RAGState:
        # Verifica JWT y extrae user_id
        state["token"] = "Token OK"
        # state["user_id"] = verify_token(state["token"])
        return state

    # Embedding Node
    # @time_execution
    def embed_node(state: RAGState) -> RAGState:
        # state["embedding"] = "embedding OK"
        state["embedding"] = embedding_query_node(state["query"])
        return state

    # Retrieval Node
    def retrieve_node(state: RAGState) -> RAGState:
        state["documents"] = retrieve_query_node(state["query"], state["embedding"])
        return state

    
    # Rerank Node
    def rerank_node(state: RAGState) -> RAGState:
        state["reranked_docs"] = rerank_query_node(state["query"], state["documents"])
        return state

    # # @observe(name="document_ingestion")
    # Generation Node
    def generateRAG_node(state: RAGState) -> RAGState:
        result = generate_answer_query_node(state["query"], state["reranked_docs"], state)

        state["prompt"] = result["prompt"]
        state["answer_context"] = result["answer_context"]


        state["response_RAG"] = result["answer_context"]

        return state
    
    
    def output_node(state: RAGState):

        state["answer_final"] = output_query_node(state["response_RAG"], state["reranked_docs"])

        return state
    
        # sources = [{"page": c.get("page", 0), "text": c["text"]} for c in state["reranked_docs"]]
        # return {
        #     "answer": state["answer"]
        # }
        # state["answer"] = [{"page": 0, "text": c} for c in state["reranked_docs"]]
        # # [{"page": 0, "text": c} for c in state["reranked_docs"]]
        # # sources = [{"page": c.get("page", 0), "text": c["text"]} for c in state["reranked_docs"]]

        # return state
    
        # return {
        #     "answer": state["answer"],
        #     "sources": sources
        #     }
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
    # from langfuse.decorators import observe
    # from langchain.callbacks.tracers.langchain import wait_for_all_tracers

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
    # query_graph = graph.compile()
    query_graph = graph.compile()


# **********************************************************************************
# **********************************************************************************
# **********************************************************************************


# import logging
# import time
# def time_execution(fn):
#     def wrapper(state):
#         start = time.time()
#         result = fn(state)
#         elapsed = time.time() - start
#         logger.info(f"[{fn.__name__}] Tiempo de ejecución: {elapsed:.2f}s")
#         return result
#     return wrapper

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