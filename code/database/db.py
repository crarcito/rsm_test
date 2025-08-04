import chromadb
from chromadb import Settings
# import chromadb.utils.embedding_functions as embedding_functions

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
    # try:
        
    # huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    #     api_key=config_env.OPENAI_API_KEY,
    #     model_name= config_env.EMBEDDING_MODEL
    # )
    
    return conexion.create_collection(
            name=config_env.CHROMA_COLLECTION,
            metadata={"hnsw:space": "cosine"}
        )

    # except Exception as ex:
    #     return None

def get_collection(conexion) -> chromadb.Collection:
    # try:
        
    return conexion.get_collection(name=config_env.CHROMA_COLLECTION)

   