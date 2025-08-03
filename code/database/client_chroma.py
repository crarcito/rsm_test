import chromadb
from chromadb import Settings
from config import config

config_env = config['default']

# client = chromadb.PersistentClient(path=config_env.CHROMA_PATH + config_env.CHROMA_DB , 
#             settings=chromadb.Settings(allow_reset=True))

# collection_get = client.get_collection(name=config_env.CHROMA_COLLECTION)
# collection_add = client.get_or_create_collection(
#                 name=config_env.CHROMA_COLLECTION,
#                 metadata={"hnsw:space": "cosine"},
#             )