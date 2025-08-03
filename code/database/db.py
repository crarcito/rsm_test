import chromadb
from chromadb import Settings
from config import config

config_env = config['default']

def get_connection():
    try:
        # return chromadb.PersistentClient(path="code/data/chroma_db", 
        return chromadb.PersistentClient(path=config_env.CHROMA_PATH + config_env.CHROMA_DB , 
            settings=chromadb.Settings(allow_reset=True)) 
   
    except Exception as ex:
        return ex
    
def create_collection(conexion):
    try:
        return conexion.create_collection(
                name=config_env.CHROMA_COLLECTION,
                metadata={"hnsw:space": "cosine"},
            )
   
    except Exception as ex:
        return ex

# def get_collection():
#     try:
#         return get_connection.get_collection(name=config_env.CHROMA_COLLECTION)
#     except Exception as ex:
#         return ex

#             ids = state["key"]
#             ids = state["key"]
# def add_to_collection(ids, documents, embeddings):
#     try:
#         collection.add(
#             documents = state["content"],
#             embeddings = state["embedding"],
#             ids = state["key"]
#         )
#     except Exception as ex:
#         return ex