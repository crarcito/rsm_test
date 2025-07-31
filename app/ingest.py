from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import dotenv
import redis

def ingest_documents():
    """Basic connection example.
    """
    # from ..config import config


    # config = config['default']
    # REDIS_URL = config.REDIS_URL
    # print("REDIS_URL:", REDIS_URL)

    # dotenv.load_dotenv()
    # REDIS_URL = os.getenv('REDIS_URL')
    # REDIS_PORT = os.getenv('REDIS_PORT')
    # REDIS_USERNAME = os.getenv('REDIS_USERNAME')
    # REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


    from config import config
    settings = config['development']
    REDIS_URL = settings.REDIS_URL
    REDIS_PORT = settings.REDIS_PORT
    REDIS_USERNAME = settings.REDIS_USERNAME
    REDIS_PASSWORD = settings.REDIS_PASSWORD
    

    conexionRedis = redis.Redis(
            host=REDIS_URL,
            port=REDIS_PORT,
            decode_responses=True,
            username=REDIS_USERNAME,
            password=REDIS_PASSWORD,
        )

    success = conexionRedis.set('foo', 'CRARCITO')

    REDIS_RETURN = conexionRedis.get('foo')


    return {
        "answer": REDIS_RETURN
,
    }

    # r = redis.Redis(
    #     host='redis-19786.c282.east-us-mz.azure.redns.redis-cloud.com',
    #     port=19786,
    #     decode_responses=True,
    #     username="default",
    #     password="Vmy82edT3gfr1WwenZy1d0xFGiEqQFht",
    # )

    # success = r.set('foo', 'bar')
    # # True

    # result = r.get('foo')
    # print(result)
    # # >>> bar



    # dotenv.load_dotenv()
    # OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # urls = [
    #     "https://allendowney.github.io/ThinkPython/index.html",
    #     "https://peps.python.org/pep-0008/"
    # ]
    # loader = WebBaseLoader(urls)
    # docs = loader.load()

    # splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    # chunks = splitter.split_documents(docs)

    # embeddings = OpenAIEmbeddings(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    # db = FAISS.from_documents(chunks, embeddings)
    # # db.save_local("vector_index")

