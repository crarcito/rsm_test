from fastapi import FastAPI, Request

from models.agents.api_test import api_router
app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():

    return {"message": "Esto es un prueba técnica para el puesto de Backend Developer en RSM."}


import logging


# @app.middleware("http")
# async def observability_middleware(request: Request, call_next):
#     logger = logging.getLogger("uvicorn")
#     logger.info(f"[REQUEST] {request.method} {request.url}")
#     response = await call_next(request)
#     logger.info(f"[RESPONSE] status={response.status_code}")
#     return response
