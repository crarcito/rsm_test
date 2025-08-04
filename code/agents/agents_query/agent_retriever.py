from openai import OpenAI
# import redis, json, numpy as np

# rdb = redis.Redis(host='localhost', port=6379)

# def cosine_similarity(v1, v2):
#     v1, v2 = np.array(v1), np.array(v2)
#     return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# def agent_retriever(state):
#     query_embedding = state["query_embedding"]
#     results = []
#     for key in rdb.scan_iter():
#         obj = json.loads(rdb.get(key))
#         score = cosine_similarity(query_embedding, obj["embedding"])
#         results.append((score, obj["content"]))
#     results.sort(reverse=True)
#     state["retrieved_texts"] = [r[1] for r in results[:3]]
#     state["trace"].span(name="retriever", input="embedding").set_output({"top_scores": [r[0] for r in results[:3]]}).end()
#     return state



# ------------

# import redis
# import json
# import numpy as np
# from embedding_factory import get_embedder

# rdb = redis.Redis(host="localhost", port=6379, decode_responses=True)
# embedder = get_embedder()

# def cosine_similarity(v1, v2):
#     v1, v2 = np.array(v1), np.array(v2)
#     return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# def agent_retriever(state):
#     query = state.get("query_rewritten", state["query"])
#     query_embedding = embedder.embed_query(query)

#     results = []
#     for key in rdb.scan_iter("doc:*"):
#         raw = rdb.get(key)
#         if not raw:
#             continue
#         try:
#             obj = json.loads(raw)
#             doc_embedding = obj["embedding"]
#             score = cosine_similarity(query_embedding, doc_embedding)
#             results.append((score, obj["content"]))
#         except Exception as e:
#             continue  # skip malformed entries

#     results.sort(reverse=True)
#     top_texts = [r[1] for r in results[:3]]
#     top_scores = [round(r[0], 4) for r in results[:3]]

#     state["retrieved_texts"] = top_texts
#     state["trace"].span(name="retriever", input=query).set_output({
#         "top_scores": top_scores,
#         "top_chunks": top_texts
#     }).end()

#     return state
