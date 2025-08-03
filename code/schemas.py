from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class QueryResponse(BaseModel):
    results: List[dict]