from fastapi import FastAPI, Request
from utils.observability import CrearArchivoLog
from models.agents.api_test import api_router
app = FastAPI()

import os
os.environ['USER_AGENT'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

CrearArchivoLog()

app.include_router(api_router)


@app.get("/")
async def root():

    return {"message": "Esto es un prueba técnica para el puesto de Backend Developer en RSM."}

