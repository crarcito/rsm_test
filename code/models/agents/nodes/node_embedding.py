from config import config

from langchain_openai import OpenAIEmbeddings

config_env = config['default']

def embedding_query_node(state):
    embedder = OpenAIEmbeddings(model=config_env.EMBEDDING_MODEL,  
                            api_key=config_env.OPENAI_API_KEY)

    embedding = embedder.embed_query(state)

    return embedding

