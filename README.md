
# 🤖 RSM Test Stack 

Este proyecto implementa una arquitectura modular para agentes conversacionales y recuperación de información, con observabilidad avanzada mediante Langfuse, trazabilidad de flujos y registro en logs local(carpeta logs). 

Incluye integración con modelos de lenguaje, embeddings, y almacenamiento en base de datos vectorial **CHROMA DB Persistent**.

Crea un asistente que responde preguntas y busca información según los criterios de búsqueda del usuario.
Su función es responder a las consultas de los usuarios sobre programación en Python, incluyendo, entre otras, fragmentos de código, bibliotecas, frameworks, mejores prácticas y depuración.


## 🚀 Características

- Ingesta de sitios web (`ThinkPython`, `PEP8`) con scraping y chunking
- Embedding semántico y almacenamiento en Chroma.
- Validación contextual vía RAG antes de responder
- PromptTemplates por modo: `explanatory`, `summary`, `critique`
- Observabilidad con Langfuse (traces, spans, feedback)
- API REST con FastAPI: `/ingest`, `/question`, `/health`


## 🧠 Arquitectura General

graph TD
    A[FastAPI App] 
    A --> B[GET /health]
    A --> B[POST /ingest]
      B --> E[Carga de documentos + Chunker]
      E --> F[Generador de Embedding]
      F --> G[Ingesta de datos como Vector (e.g. CHROMADB)]
    A --> C[POST /query]
      C --> H[Retriever]
      H --> I[LLM via LangChain]
      I --> J[Langufuse Observability]

## 🛠 Tecnologías

LangGraph	  Orquestación modular de nodos RAG
FastAPI     API web para interacción y visualización
CHROMA      Almacenamiento y recuperación semántica de embeddings
LangChain   Interfaz con LLMs y retrievers
Langfuse    Trazabilidad por spans en cada etapa del grafo
Prometheus  Métricas de latencia, errores y uso de LLM (a futuro)



## 📦 Estructura del proyecto

rsm_test/
├── code/
│   └── data/
│       └── test_chroma       # Base de datos chroma
│   └── database/
│       └── db.py             # Conexión a base de datos
│   └── models/
│       └── agents/
│       └── nodes_ingest/
│       └── nodes_query/
│   └── utils/
│   └── ...
├── logs/
├── requirements.txt
├── Dockerfile
├── .env
├── langgraph.json
└── main.py


## 📡 Endpoints REST

GET	      /health	    Verifica estado del servicio
POST	    /ingest	    Creación de base de datos e Ingesta de documentos web
POST	    /query	    Consulta a LLM con RAG, enviar pregunta en JSON: { "question": "..." }



## 🚀 Instalación y despliegue

### 1- Clonar repositorio desde github con README y .gitignore
  . git clone https://github.com/carlos-ai/langgraph-rag-enhanced.git

### 2- Crear virtualenv
  - python -m virtualenv env
  - .\env\Scripts\activate

### 3. Actualizar Variables de entorno
- Agrega el archivo `.env` (puedes copiar de `.env.template`) y actualiza las claves necesarias:

- `OPENAI_API_KEY`
- `LANGFUSE_SECRET_KEY`
- `LANGFUSE_PUBLIC_KEY`
- `LANGSMITH_API_KEY`
- `LANGCHAIN_API_KEY`
- `GITHUB_TOKEN_PAT` (solo si usas GitHub Actions)

### 4. Prueba en ambiente de desarrollo

- Ejecuta el servidor FastAPI:
```sh
pip install -r requirements.txt
fastapi dev code/main.py

  accede a http://127.0.0.1:8000/docs
  o puedes consumirla directo desde algún software como postman
    http://127.0.0.1:8000/query?question=que es PEP?
```

- Ejecuta el agente LangGraph en modo desarrollo:
```sh
pip install -r requirements.txt
langgraph dev
- Link a Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

- Puedes acceder a un sitio web local de pruebas desarrollado para este caso, solo puedes hacer consultas
```sh
pip install -r requirements.txt   # primero instala las dependencias
python code/test.py               # luego inicia el sitio

  accede al servidor que te indica, por lo regular es 
      http://127.0.0.1:7103
```


### 5. 🐳 Docker Setup

#### - Crear imagen y probar localmente
```sh
docker build -t rsm/fastapi-test:latest .
docker run -p 8000:8000 rsm/fastapi-test:latest
```
- Publicar en Docker Hub
```sh
docker login
docker push rsm/fastapi-test:latest
```

- Configuración en Azure Web App
  Registry Server URL: https://index.docker.io
  Image and Tag: rsm/fastapi-test:latest


### 6. Docker Compose
```sh
docker compose -f docker-compose.yaml down
```

> **Nota:** Para probar el funcionamiento de ingest se debe cambiar el valor de `CHROMA_DB=nuevo_nombre` en el archivo de entorno.

### 7. Ejecución en local
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```


## 📌 Justificación Técnica

- LangGraph permite bifurcaciones, ciclos y control de flujos multi-nodo de forma declarativa.
- ChromaDB Persistent proporciona búsquedas semánticas escalables sin necesidad de FAISS externo.
- FastAPI + Langfuse combinan trazabilidad, métricas y estructura productiva lista para monitoreo real.
- Separación modular de nodos, validación de respuestas, reformulación y fallback mejoran la calidad sustancial del servicio.


## 🛠 Extensiones futuras
- Reescritura contextual automática con feedback humano
- Exportación de logs y métricas a ELK / Grafana
- Autenticación de endpoints y control por token
- Interfaz visual (Flask/Streamlit) para usuarios finales
- Observabilidad con Prometheus (GET /metrics	  Métricas Prometheus)
- Flujo multiagente con LangGraph: rewriter, evaluator, retriever, synthesizer, critic


## 📊 Observabilidad

La integración con Langfuse permite trazabilidad avanzada de los flujos y agentes. Consulta la documentación interna en `code/utils/observability.py` para personalizar la instrumentación.

---

---
## Créditos y licencias

- [LangChain](https://github.com/langchain-ai/langchain)
- [Langfuse](https://langfuse.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)


## 📣 Contacto

**Carlos** — Desarrollador de sistemas con enfoque en arquitectura modular, escalabilidad y transparencia en flujos de IA.  
Este proyecto refleja mis habilidades en:

- Diseño de microservicios con FastAPI
- Orquestación de flujos LLM con LangGraph
- Observabilidad con Langfuse
- Integración con bases vectoriales empresariales (CHOMADB PERSISTENT)
- Buenas prácticas de arquitectura modular, logging estructurado y documentación

📧 craralvarez@hotmail.com 🔗 LinkedIn · GitHub
---

Este proyecto se distribuye bajo la licencia MIT.

