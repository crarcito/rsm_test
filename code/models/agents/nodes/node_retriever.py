import json
from config import config

from database.db import get_connection, get_collection

from config import config
config_env = config['default']

def retrieve_query_node(question, state):

    # question = state["query"]
    # return question
    if not question:
        raise ValueError("No question provided")

    connection  = get_connection()
    collections = get_collection(connection)

    results = collections.query(
            query_texts=[question],
            n_results=5,
            include=["documents", "metadatas"]
        )
    if not results or "documents" not in results or not results["documents"]:
        raise ValueError("No documents found in the results")
    

    if not results or "documents" not in results or not results["documents"]:
        raise ValueError(["No documents found in the results"])
    # Assuming results["documents"] is a list of documents
    if not results["documents"][0]:
        raise ValueError(["First document is empty"])
    
    retrieved_documents = results['documents'][0]

    # Clean the documents
    # clean_texts = [doc.count for doc in retrieved_documents]
    # clean_texts[:2]



    return retrieved_documents

