# test_rsm run 

### DEPLOY A DOCKER IMAGE , PUSH TO DOCKER HUB AND AZURE
## Creación docker para push en Docker Hub:
    docker build -t rsm/fastapi-test:latest .
  
## Prueba Local de la Imagen Docker:

    Probamos nuestra imagen Docker localmente para asegurarnos de que la aplicación funciona:

    docker run -p 8000:8000 rsm/fastapi-test:latest


## Inicio de Sesión en Docker Hub:

    Iniciamos sesión en Docker Hub para poder subir la imagen:
      docker login
    Publicación de la Imagen en Docker Hub:

    Subimos nuestra imagen al repositorio público de Docker Hub:

      docker push rsm/fastapi-test:latest
  
  
## Configuración en Azure Web App:

    Configuramos nuestro Azure Web App para usar la imagen de Docker Hub:
      Registry Server URL: https://index.docker.io
      Image and Tag: rsm/fastapi-test:latest


### Pruebas en ambiente de desarrollo
## Run agent langgraph   en dev
      - langgraph dev

## Run fastapi server 
      - fastapi dev code/main_test.py

## Docker
      docker run -p 8000:8000 rsm/fastapi-test:latest

      docker compose -f docker-compose.yaml down

      ### para probar el funcionamiento de ingest se debe cambiar el valor de CHROMA_DB=nuevo_nombre

## Prueba en local CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

---------------------------------------------------------------------------
### Instrucciones generales

   
## OK 4.- Agregar .env (variables de entorno)
     - Varias (copiar de .env.template)
     - Actualizar APIS y keys necesarias como:
         - OPENAI_API_KEY
         - GITHUB_TOKEN_PAT   -> solo si se usa Actions de github
         - LANGSMITH_API_KEY
         - LANGCHAIN_API_KEY
         - LANGFUSE_SECRET_KEY
         - LANGFUSE_PUBLIC_KEY
     


## OK 7.- Probar que funcione en local con 
      pip install -r requirements.txt
      cd code -> uvicorn main:app --reload

      ### Run agent
      - langgraph dev

      ### Run fastapi server
      - fastapi dev code/main_test.py

        
