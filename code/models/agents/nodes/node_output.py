from typing import List, TypedDict

import utils.prompts as prompts

def output_query_node(response_RAG: str, docs: List[str]) -> dict:


    results = {
            "answer": response_RAG,
            "sources": [{"page": 0, "text": c} for c in docs]
        }

    return results