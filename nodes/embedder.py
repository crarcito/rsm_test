import openai
from langchain.embeddings import OpenAIEmbeddings
from config import config

settings = config['development']

def get_embedder(model_name: str | None = None) -> OpenAIEmbeddings:
    """
    Factory to create an embedding model instance.
    Reads model name from argument or environment variable.
    """
    model = settings.EMBEDDING_MODEL or "text-embedding-ada-002"

    # You can extend this to support other providers later
    return OpenAIEmbeddings(model=model)


def embed_node(state):
    content = state["content"]
    #     embeddings = OpenAIEmbeddings(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    #     # db = FAISS.from_documents(chunks, embeddings)
    #     # # db.save_local("vector_index")

    embedder = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=settings.OPENAI_API_KEY)
    state["embedding"] = embedder.embed_query(content)

    # # response = openai.Embedding.create(model="text-embedding-ada-002", input=content)
    # state["embedding"] = response["data"][0]["embedding"]
    # return state
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=OPENAI_API_KEY)
    # state["embedding"] = get_embedder().embed_query(content)
    return state


