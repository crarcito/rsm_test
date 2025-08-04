from openai import OpenAI
from typing import List, TypedDict


from langgraph.graph import StateGraph, START, END
# from langgraph.graph.message import Message
# from langfuse.decorators import observe, langfuse_context

from langchain_openai import ChatOpenAI

# from langfuse.decorators import langfuse_context, observe


from models.nodes_query.embedding import embedding_query_node
from models.nodes_query.retrieve import retrieve_query_node





import chromadb 

# lf = Langfuse(public_key="...", secret_key="...")

# Define state
class RAGState(TypedDict):
    query: str
    token: str

    embedding: List[float]
    documents: List[str]
    reranked_docs: list[str]

    answer: str

    # query: str
    # user_id: str
    # embedding: list[float]
    # documents: list[str]
    # reranked_docs: list[str]
    # answer: str 



# Auth Node
def auth_node(state: RAGState) -> RAGState:
    # Verifica JWT y extrae user_id
    state["token"] = "Token OK"
    # state["user_id"] = verify_token(state["token"])
    return state



# Embedding Node
def embed_node(state: RAGState) -> RAGState:
    # state["embedding"] = "embedding OK"
    state["embedding"] = embedding_query_node(state["query"])
    return state

# Retrieval Node
def retrieve_node(state: RAGState) -> RAGState:
    state["documents"] = retrieve_query_node(state["query"], state["embedding"])
    return state

# # Rerank Node
def rerank_node(state: RAGState) -> RAGState:
    state["reranked_docs"] = rerank(state["query"], state["documents"])
    return state

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


graph = StateGraph(RAGState)

graph.add_node("auth", auth_node)
graph.add_node("embed", embed_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("rerank", rerank_node)
# graph.add_node("generate", generate_node)
# graph.add_node("feedback", feedback_node)
# graph.add_node("output", output_node)

graph.set_entry_point("auth")
graph.add_edge("auth", "embed")
graph.add_edge("embed", "retrieve")
graph.add_edge("retrieve", "rerank")
# graph.add_edge("rerank", "generate")
# graph.add_edge("generate", "feedback")
# graph.add_edge("feedback", "output")
# graph.add_edge("output", END)
graph.add_edge("rerank", END)


# Compile the graph
rsm_graph = graph.compile()



