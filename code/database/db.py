import chromadb

from config import config
config_env = config['default']

import utils.time as tiempo

# Conexión o creación base de datos
@tiempo.time_execution
def get_connection(urls):
    try:
        # return chromadb.PersistentClient(path="code/data/chroma_db", 
        return chromadb.PersistentClient(path=config_env.CHROMA_PATH + config_env.CHROMA_DB) 

    except Exception as ex:
        return ex
    
# Creación tabla o Collection de base de datos
@tiempo.time_execution    
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

# Obtiene collection
@tiempo.time_execution
def get_collection(conexion) -> chromadb.Collection:
    # try:
        
    return conexion.get_collection(name=config_env.CHROMA_COLLECTION)

