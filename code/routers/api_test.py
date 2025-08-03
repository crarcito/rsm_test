from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health/")
async def health():
    return {"status": "200 OK"}

@api_router.get("/ingest/")
async def ingest():
    return {"message": "List of items"}

@api_router.get("/query/{item_id}")
async def readquery_item(item_id: int):
    return {"item_id": item_id}