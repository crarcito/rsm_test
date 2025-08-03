FROM python:3.10-slim
# FROM python:3.12.5-alpine

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

CMD ["python", "code/app.py"]