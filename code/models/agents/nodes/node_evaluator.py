from openai import OpenAI
# import redis, json, numpy as np
# from nodes.embedder import embed_node

# rdb = redis.Redis(host='localhost', port=6379)

# def cosine_similarity(v1, v2):
#     v1, v2 = np.array(v1), np.array(v2)
#     return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# def agent_evaluator(state):
#     query = state["query_rewritten"]
#     query_embedding = embed_node({"content": query})["embedding"]
#     max_score = max(
#         cosine_similarity(query_embedding, json.loads(rdb.get(k))["embedding"])
#         for k in rdb.scan_iter()
#     )
#     state["query_embedding"] = query_embedding
#     state["valid"] = max_score > 0.75
#     state["similarity_score"] = round(max_score, 4)
#     state["trace"].span(name="evaluator", input=query).set_output({"score": max_score}).end()
#     return state
