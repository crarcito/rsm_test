##### DEPLOY A DOCKER IMAGE TO A SERVER USING GITHUB ACTIONS.

## test_rsm
---------------------------------------------------------------------------
### Instrucciones general

##### OK 1.- Crear clave SSH usando SSh Keygen  (https://www.youtube.com/watch?v=CE16RyFDW_M)
##### OK 2.- Crear en github TOKEN PAT -> xxxx    usuario : xxxxx
##### OK 3.- Copiar las instrucciones en README

### Instrucciones proyecto
##### OK 1.- Crear repositorio en github con README y .gitignore de VS
##### OK 2.- Clonar con github desktop
##### OK 3.- Crear virtualenv
     - instalar  python -m virtualenv env
     - ejecutar  .\env\Scripts\activate
     - chequear que aparezca (env) en la terminal con PS
     
##### OK 4.- Agregar .env (variables de entorno)
     - Varias (copiar de .env.template)
     
##### OK 5.- Crear estructura de carpetas
      - code
         - app.py (algo)
         - config.py
         - database
         - models
         - routes
         - utils

##### OK 6.- Agregar requirements.txt
        openai
        langchain_openai
        autopep8==1.6.0
        click==8.1.2
        colorama==0.4.4
        importlib-metadata==4.11.3
        itsdangerous==2.1.2
        Jinja2==3.1.1
        MarkupSafe==2.1.1
        pycodestyle==2.8.0
        python-decouple
        python-dotenv
        psycopg2-binary
        six==1.16.0
        toml==0.10.2
        Werkzeug==2.1.1
        zipp==3.8.0
        wget==3.2
        pandas
        fuzzywuzzy==0.18.0
        pgvector

##### OK 7.- Probar que funcione en local con 
      pip install -r requirements.txt
      python3 code/main_test.py

      ### Run agent
      - langgraph dev

      ### Run fastapi server
      - fastapi dev code/main_test.py

        
##### OK 8.- Agregar Dockerfile con la estructura
    FROM python:3.10-slim

    WORKDIR /app

    COPY code /app/code

    # RUN apk add --no-cache gcc musl-dev linux-headers

    COPY .env  .env

    COPY requirements.txt  requirements.txt

    RUN pip install --no-cache-dir -r requirements.txt


    RUN pip3 install transformers --no-deps \
        && pip3 install torch --no-deps  --index-url https://download.pytorch.org/whl/cpu \
        && pip3 install sentence-transformers

    RUN python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('sdadas/mmlw-retrieval-roberta-large')"

    CMD ["python", "code/main_test.py"]


##### OK 9.- Crear carpetas y workflow para Actions de GitHub
       .github
            workflows
                  builddockerimg.yml (basarse en estructura original de más abajo)
                        ->Definir variables
                              TAG: (repositorio)
                              TAG_NEW: (nombre para composer)
                              PAT: ${{ secrets.GITHUB_TOKEN }}
                              USER: (cuenta github Ej: crarcito)
                              REGISTRY: ghcr.io
                              VERSION: v1

##### OK 10.- Crear secrets de repositorio en GitHub
       SSH_HOST = 
       SSH_USER = root
       SSH_PRIVATE_KEY =  rd_isa  (basarse en texto de más abajo)
       SSH_PORT = 
       WORK_DIR = 


##### OK 11.- Crear compose en Dockge apuntando a un puerto 710x  (dockge.allgest.cl)
       docker-compose.yaml
            services:
            web:
                container_name: test-rsm
                image: test-rsm_api:v1
                restart: unless-stopped
                environment:
                    mismo de .env
                ports:
                - 7103:7103
            networks: {}

             agregar vol:  network:   si corresponde


##### OK 14.- Crear subdominio en DNS VPS
      - Crear subdominio en : subdominio.dominio.cl apuntando a la IP Pública que corresponda
##### OK 15.- Crear Proxy Host em Nginx
      - Con datos del subdominio del punto 15  ( en proxy.xxx.cl )
      - No olvidar Https (Forzar)

##### OK 16.- Chequear permisos para GITHUB_TOKEN en github
      - Repositorio->Setting->Action->General-> 
          Allow all actions and reusable workflows (check) -> Save
          Workflow permissions  (check)
          Allow GitHub Actions to create and approve pull requests (check)
          Save
          No tienen que existir packages

##### OK 17.- Commit y Push a github

##### OK 18.-  Chequear jobs de Action
      - La primera vez se caerá, porque no existe el compose
      - Iniciar compose de dockge

##### OK 19.- Chequear imagen creada en VPS
        docker images

##### OK 20.- Abrir y chequear subdominio.dominio.cl



-----
##### builddockerimg.yml
      name: buid and deploy docker image
      on:
        push:
          branches:
            - main
        workflow_dispatch:
      jobs:
        build_docker_img:
          name: Build Docker Image
          runs-on: ubuntu-latest
          env:
            TAG: test-rsm
            TAG_COMPOSE: testrsm
            PAT: ${{ secrets.GITHUB_TOKEN }}
            USER: 
            REGISTRY: ghcr.io
            VERSION: v1

          steps:
            - name: Checkout code
              uses: actions/checkout@v2

            - name: Build Docker Image
              run: docker build -t $TAG .

            - name: Login to gHCR
              run: |
                echo $PAT | docker login ${{ env.REGISTRY }} -u $USER --password-stdin
                docker tag $TAG ${{ env.REGISTRY }}/$USER/$TAG:${{ env.VERSION }}
                docker push ${{ env.REGISTRY }}/$USER/$TAG:${{ env.VERSION }}

        deploy:
          needs: build_docker_img
          name: deploy and publish image to server
          runs-on: ubuntu-latest
          env:
            TAG: test-rsm
            TAG_COMPOSE: test_rsm
            PAT: ${{ secrets.GITHUB_TOKEN }}
            USER: 
            REGISTRY: ghcr.io
            VERSION: v1

          steps:
            - name: install ssh keys, connect to github, pull image new, rmi image old, stop and start container
              uses: appleboy/ssh-action@v1.0.0            
              with:
                host: ${{ secrets.SSH_HOST }}
                username: ${{ secrets.SSH_USER }}
                key: ${{ secrets.SSH_PRIVATE_KEY }}
                port: ${{ secrets.SSH_PORT }}
                before_script:              
                  echo $PAT | docker login ${{ env.REGISTRY }} -u $USER --password-stdin
                script: |
                  cd ${{ secrets.WORK_DIR }}
                  docker pull ${{ env.REGISTRY }}/${{ env.USER }}/${{ env.TAG }}:${{ env.VERSION }}
                  docker compose kill
                  docker rmi ${{ env.TAG_COMPOSE }}:${{ env.VERSION }} --force
                  docker tag ${{ env.REGISTRY }}/${{ env.USER }}/${{ env.TAG }}:${{ env.VERSION }} ${{ env.TAG_COMPOSE }}:${{ env.VERSION }}
                  docker rmi ${{ env.REGISTRY }}/${{ env.USER }}/${{ env.TAG }}:${{ env.VERSION }} --force
                  docker compose start
                  exit
                
# ---------------------------
# HASTA AQUI EN README
# ---------------------------
