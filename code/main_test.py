from config import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.api_test import api_router

app = FastAPI()

# print(__name__)
if __name__ == 'main_test':
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    @app.get("/")
    async def root():
        return {"message": "Esto es un prueba técnica para el puesto de Backend Developer en RSM."}

