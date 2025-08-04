import json
from config import config

import chromadb


config_env = config['default']

def store_node(state, collection_test: chromadb.Collection):
    """Store the node in Chroma."""
    if "content" not in state or "embedding" not in state:
        raise ValueError("State must contain 'content' and 'embedding' keys.")

    key = state["key"]

    try:                
        # Store the content and embedding in Chroma
        collection_test.add(
            documents = state["content"],
            embeddings = state["embedding"],
            ids = state["key"]
        )
    except Exception as ex:
        raise ex
    return state
