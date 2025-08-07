from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_query_node(query: str, docs: list[str], top_k: int = 3) -> list[str]:
    # Crear pares (query, doc)
    pairs = [[query, doc] for doc in docs]

    # Obtener scores
    scores = reranker.predict(pairs)

    # Ordenar documentos por score
    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    # Guardar top-k rerankeados
    return [doc for doc, _ in ranked[:top_k]]
