from config import config

from chromadb import Collection
from langchain_openai import OpenAIEmbeddings

config_env = config['default']

def query_node(state, collection_test, matching_count):
    # try:                
        # embedder = OpenAIEmbeddings(model=config_env.EMBEDDING_MODEL,  
        #                         api_key=config_env.OPENAI_API_KEY)
        
        # embedding = embedder.embed_query(question)
        # results = collection_test.query(
        #             query_texts=[question],
        #             n_results=matching_count
        #         )
        
        # results = collection_test.query(
        #         query_embeddings=[embedding],
        #         n_results=matching_count
        #     )
    results = collection_test.query(
        query_texts=[state],
        n_results=matching_count,
        include=["documents", "metadatas"]
    )
    documents = results["documents"][0]

    clean_texts = [t.page_content for t in documents]
    clean_texts[:2]

    
    # docs = chroma_retrieve(state["query"], collection_test, top_k=5)
    state["sources"] = [{"page": i + 1, "text": doc} for i, doc in enumerate(documents)]
    docs = state


    # answer

    return docs
    


        # reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        # results = collection_test.query(
        #             query_texts=[question],
        #             query_embeddings=[embedding],
        #             n_results=matching_count
        #         )        
        # collection.query(
                    #     query_embeddings=[[11.1, 12.1, 13.1],[1.1, 2.3, 3.2], ...],
                    #     n_results=5,
                    #     where={"page": 10}, # query records with metadata field 'page' equal to 10
                    #     where_document={"$contains": "search string"} # query records with the search string in the records' document
                    # )

    # except Exception as ex:
    #     raise ex
    
    # return retrieved

def chroma_retrieve(query: str, collection_test, top_k: int = 5) -> list[dict]:
    results = collection_test.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas"]
    )

    documents = results["documents"][0]

    return documents

