from nodes.scraper import scrape_node
from nodes.chunker import chunk_text
from nodes.embedder import embed_node
from nodes.store_redis import store_node


def ingest_urls(urls: list[str]):
    """ Ingests a list of URLs by scraping, chunking, embedding, and storing the content."""
    if not urls:
        raise ValueError("No URLs provided for ingestion.")
    
    #     loader = WebBaseLoader(urls)
    #     docs = loader.load()
    


    for i, url in enumerate(urls):
        state = {"url": url, "key": f"doc:{i}"}

        scrape_node(state)
        chunk_text(state)        
        for chunk in state["chunks"]:
            chunk_state = {"content": chunk, "key": f"doc:{i}:{hash(chunk)}"}
            embed_node(chunk_state)
            store_node(chunk_state)
    return {
        "status_ingest": chunk_state,
        }


# def ingest_documents():
#     """Basic connection example.
#     """
#     # from ..config import config


#     # config = config['default']
#     # REDIS_URL = config.REDIS_URL
#     # print("REDIS_URL:", REDIS_URL)

#     # dotenv.load_dotenv()
#     # REDIS_URL = os.getenv('REDIS_URL')
#     # REDIS_PORT = os.getenv('REDIS_PORT')
#     # REDIS_USERNAME = os.getenv('REDIS_USERNAME')
#     # REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


#     from config import config
#     settings = config['development']
#     REDIS_URL = settings.REDIS_URL
#     REDIS_PORT = settings.REDIS_PORT
#     REDIS_USERNAME = settings.REDIS_USERNAME
#     REDIS_PASSWORD = settings.REDIS_PASSWORD
    

#     conexionRedis = redis.Redis(
#             host=REDIS_URL,
#             port=REDIS_PORT,
#             decode_responses=True,
#             username=REDIS_USERNAME,
#             password=REDIS_PASSWORD,
#         )

#     # success = conexionRedis.set('foo', 'CRARCITO')

#     # REDIS_RETURN = conexionRedis.get('foo')


#     from langchain.document_loaders import WebBaseLoader
#     from langchain.text_splitter import RecursiveCharacterTextSplitter
#     from langchain.embeddings import OpenAIEmbeddings
#     from langchain.vectorstores import FAISS


#     urls = [
#         "https://allendowney.github.io/ThinkPython/index.html",
#         "https://peps.python.org/pep-0008/"
#     ]
#     loader = WebBaseLoader(urls)
#     docs = loader.load()

#     splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     chunks = splitter.split_documents(docs)

#     embeddings = OpenAIEmbeddings(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
# #     # db = FAISS.from_documents(chunks, embeddings)
# #     # # db.save_local("vector_index")

#     return {
#         "answer": REDIS_RETURN
# ,
#     }
