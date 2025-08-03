import json
from config import config



config_env = config['default']

def store_node(state, collection_test):
    """Store the node in Chroma."""
    if "content" not in state or "embedding" not in state:
        raise ValueError("State must contain 'content' and 'embedding' keys.")

    key = state["key"]

    try:                
        # Store the content and embedding in Chroma
        # collection_add = client.get_or_create_collection(
        #         name=config_env.CHROMA_COLLECTION,
        #         metadata={"hnsw:space": "cosine"},
        #     )
        collection_test.add(
            documents = state["content"],
            embeddings = state["embedding"],
            ids = state["key"]
        )
    except Exception as ex:
        raise ex
    return state
