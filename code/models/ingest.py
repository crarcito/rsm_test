from config import config
from utils.observability import start_trace, log_span, log_error, CrearArchivoLog
from datetime import datetime
import logging

from models.nodes_ingest import scraper, chunker, embedder, store_chroma

# from nodes_ingest.scraper import scrape_node

from database.db import get_connection, create_collection

config_env = config['default']


from chromadb import Collection

class Ingestion():    
    @classmethod
    def add_ingest_urls(self):
    # try:
        CrearArchivoLog()

        logger = logging.getLogger('test_rsm')

        urls = [config_env.URL_1, config_env.URL_2]

        datetime_now = str(datetime.now())

        trace = start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text="Conectando al servidor", seed=datetime_now, output_text={"docs":urls})

        urls = [config_env.URL_1, config_env.URL_2]

        # urls = ["https://www.google.com/"]

        if not urls:
            logger.error('No URLs provided for ingestion. (add_ingest_urls)')
            raise ValueError("No URLs provided for ingestion. (add_ingest_urls)")

        try:

            logger.info(f"Iniciando creación de base de datos {config_env.CHROMA_DB}")
            start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text="Conectando al servidor...", seed=datetime_now, output_text={"docs":urls})
            connection  = get_connection()
            start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text="Creando base de datos...", seed=datetime_now, output_text={"docs":urls})


            start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"Creando Collection {config_env.CHROMA_COLLECTION} ...", seed=datetime_now, output_text={"docs":urls})
            collections = create_collection(connection)

            start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"Ingestion datos en Collection {config_env.CHROMA_COLLECTION} ...", seed=datetime_now, output_text={"docs":urls})

            for i, url in enumerate(urls):
                state = {"url": url, "key": f"doc:{i}"}

                start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"Iniciando scrapping a documento {url}...", seed=datetime_now, output_text=url)
                scraper.scrape_node(state)

                start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"scrapping terminado -> Iniciando chunking ...", seed=datetime_now, output_text=url)
                chunker.chunk_text(state)

                start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"chunking terminado -> Iniciando embedding ...", seed=datetime_now, output_text=url)

                for chunk in state["chunks"]:
                    chunk_state = {"content": chunk, "key": f"doc:{i}:{hash(chunk)}"}
                    embedding_chunk = embedder.embed_node(chunk_state)
                    # store_chroma.store_node(chunk_state, collections)

                    key = state["key"]

                    # Store the content and embedding in Chroma
                    collections.add(
                        documents = chunk_state["content"],
                        ids = state["key"]
                    )

            start_trace(user_id="crar", name=f"Creación de base de datos {config_env.CHROMA_DB}", input_text=f"Proceso creación de base de datos terminada", seed=datetime_now, output_text={"docs":urls})
            logger.info(f"Creación de base de datos {config_env.CHROMA_DB} terminada con éxito")

        except ValueError as ex:
            logger.error(f"Error en la creación de base de datos {config_env.CHROMA_DB} - {ex.args}")
        

        return {
                "status_ingest": "ingested ok",
                }
