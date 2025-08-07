FROM python:3.11-slim
# FROM python:3.12.5-alpine

WORKDIR /app

COPY code /app/code

# RUN apk add --no-cache gcc musl-dev linux-headers

COPY .env  .env

ENV USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

COPY requirements.txt  requirements.txt

RUN pip install -r requirements.txt


RUN pip3 install transformers --no-deps \
    && pip3 install torch --no-deps  --index-url https://download.pytorch.org/whl/cpu \
    && pip3 install sentence-transformers

RUN python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('sdadas/mmlw-retrieval-roberta-large')"

CMD ["python", "code/test.py"]

# Run uvicorn server when the container launches
# CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]