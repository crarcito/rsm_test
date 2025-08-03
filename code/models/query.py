import chromadb

from database.db import get_connection
from config import config

config_env = config['default']


class Query():
    @classmethod
    def get_question_answer(self, question, matching_count):
        try:
            collection = get_connection()
            # collection = conecction.get_collection(name="test_collection")

            # results = collection.query(
            #         query_texts=[question],
            #         n_results=matching_count
            #     )
            results = "nose"
            return results
        except Exception as ex:
            return ex

        
        