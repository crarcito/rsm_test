from config import config
from utils.observability import start_trace, log_span, log_error, CrearArchivoLog
from datetime import datetime

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

        urls = [config_env.URL_1, config_env.URL_2]

        # urls = ["https://www.google.com/"]

        if not urls:
            raise ValueError("No URLs provided for ingestion. (add_ingest_urls)")

        connection  = get_connection()
        collections = create_collection(connection)

        for i, url in enumerate(urls):
            state = {"url": url, "key": f"doc:{i}"}

            trace = start_trace(user_id="crar", name="start scrape_node documento", input_text=state["url"], seed=str(datetime.now()), output_text=dict())
            scraper.scrape_node(state)
            trace = start_trace(user_id="crar", name="end scrape_node documento", input_text=state["url"], seed=str(datetime.now()), output_text=dict())

            trace = start_trace(user_id="crar", name="start chunker_text", input_text=state["url"], seed=str(datetime.now()), output_text=dict())
            chunker.chunk_text(state)
            trace = start_trace(user_id="crar", name="end chunker_text", input_text=state["url"], seed=str(datetime.now()), output_text=dict())

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
                # collection.add(
                #     ids=["id1", "id2", "id3", ...],
                #     embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],
                #     documents=["doc1", "doc2", "doc3", ...],
                #     metadatas=[{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}, ...],
                    
                # )


    # except ValueError as ex:
    #     raise ex
        
        return {
                "status_ingest": "ingested",
                }
