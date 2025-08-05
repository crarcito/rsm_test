# import numpy as np
# import json
# import redis
# from nodes.embedder import embed_node

# rdb = redis.Redis(host='localhost', port=6379)

# def cosine_similarity(v1, v2):
#     v1, v2 = np.array(v1), np.array(v2)
#     return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# def validate_query_context(state):
#     query = state["query"]
#     query_embedding = embed_node({"content": query})["embedding"]
#     threshold = 0.75
#     max_score = float('-inf')

#     for key in rdb.scan_iter():
#         obj = json.loads(rdb.get(key))
#         score = cosine_similarity(query_embedding, obj["embedding"])
#         max_score = max(max_score, score)

#     state["query_embedding"] = query_embedding
#     state["valid"] = max_score >= threshold
#     state["similarity_score"] = round(max_score, 4)

#     if not state["valid"]:
#         state["error"] = (
#             f"La pregunta no parece estar relacionada con el contenido indexado. "
#             f"Máxima similitud: {state['similarity_score']} (< {threshold})"
#         )

#     return state