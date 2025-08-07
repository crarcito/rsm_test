from models.nodes_query import queries
from database.db import get_connection, get_collection

from config import config

config_env = config['default']

import utils.time as tiempo
@tiempo.time_execution
class Query():
    @classmethod
    def get_question_answer(self, question, matching_count):
        try:
            if not question:
                raise ValueError("No question provided")
    
            connection  = get_connection("")
            collections = get_collection(connection)

            state = {"query": question}


            results = queries.query_node(question, collections, matching_count)

            # results = "nose"
            return results
        except ValueError as ex:
            return ex

        
        