from langchain_openai import OpenAIEmbeddings

from config import config
config_env = config['default']

import utils.time as tiempo

@tiempo.time_execution
def embed_node(state):
    content = state["content"]

    # dimensions=1536   384
    embedder = OpenAIEmbeddings(model=config_env.EMBEDDING_MODEL,  
                                api_key=config_env.OPENAI_API_KEY)
    state["embedding"] = embedder.embed_query(content)

    # # response = openai.Embedding.create(model="text-embedding-ada-002", input=content)
    # state["embedding"] = response["data"][0]["embedding"]
    # return state
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=OPENAI_API_KEY)
    # state["embedding"] = get_embedder().embed_query(content)
    return state


