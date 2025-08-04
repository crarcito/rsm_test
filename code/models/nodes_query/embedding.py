import json
from config import config

from langchain_openai import OpenAIEmbeddings

config_env = config['default']

def embedding_query_node(state):
    try:                
        embedder = OpenAIEmbeddings(model=config_env.EMBEDDING_MODEL,  
                                api_key=config_env.OPENAI_API_KEY)

        # embedding = "bien"
        embedding = embedder.embed_query(state)

    except Exception as ex:
        raise ex

    return embedding

