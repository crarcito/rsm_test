# RSM Test Stack

Proyecto de referencia para la integración de agentes, trazabilidad y recuperación de información usando Python, LangChain, Langfuse y Sentence Transformers.

---

## Descripción

Este proyecto implementa una arquitectura modular para agentes conversacionales y recuperación de información, con observabilidad avanzada mediante Langfuse y trazabilidad de flujos. Incluye integración con modelos de lenguaje, embeddings, y almacenamiento en Redis y FAISS.

---

## Estructura del proyecto

```
rsm_test/
├── code/
│   ├── agents/
│   ├── models/
│   ├── utils/
│   └── ...
├── requirements.txt
├── Dockerfile
├── .env
└── main.py
```

---

## Instalación y despliegue

### 1. Variables de entorno

Agrega el archivo `.env` (puedes copiar de `.env.template`) y actualiza las claves necesarias:

- `OPENAI_API_KEY`
- `LANGFUSE_SECRET_KEY`
- `LANGFUSE_PUBLIC_KEY`
- `LANGSMITH_API_KEY`
- `LANGCHAIN_API_KEY`
- `GITHUB_TOKEN_PAT` (solo si usas GitHub Actions)

---

### 2. Instalación local

```sh
pip install -r requirements.txt
cd code
uvicorn main:app --reload
```

---

### 3. Pruebas en ambiente de desarrollo

- Ejecuta el agente LangGraph en modo desarrollo:
  ```sh
  langgraph dev
  ```
- Ejecuta el servidor FastAPI:
  ```sh
  fastapi dev code/main_test.py
  ```

---

### 4. Docker

#### Crear imagen y probar localmente

```sh
docker build -t rsm/fastapi-test:latest .
docker run -p 8000:8000 rsm/fastapi-test:latest
```

#### Publicar en Docker Hub

```sh
docker login
docker push rsm/fastapi-test:latest
```

#### Configuración en Azure Web App

- Registry Server URL: https://index.docker.io
- Image and Tag: rsm/fastapi-test:latest

#### Docker Compose

```sh
docker compose -f docker-compose.yaml down
```

> **Nota:** Para probar el funcionamiento de ingest se debe cambiar el valor de `CHROMA_DB=nuevo_nombre` en el archivo de entorno.

---

### 5. Ejecución en local

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## Observabilidad

La integración con Langfuse permite trazabilidad avanzada de los flujos y agentes. Consulta la documentación interna en `code/utils/observability.py` para personalizar la instrumentación.

---

## Créditos y licencias

- [LangChain](https://github.com/langchain-ai/langchain)
- [Langfuse](https://langfuse.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)

Este proyecto se distribuye bajo la licencia MIT.

---

¿Tienes dudas o sugerencias? Abre un issue o contacta al equipo de desarrollo.