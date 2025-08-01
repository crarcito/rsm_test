import redis, json
from config import config


settings = config['development']

conexionRedis = redis.Redis(
        host=settings.REDIS_URL,
        port=settings.REDIS_PORT,
        decode_responses=True,
        username=settings.REDIS_USERNAME,
        password=settings.REDIS_PASSWORD,
    )

def store_node(state):
    """Store the node in Redis."""
    if "content" not in state or "embedding" not in state:
        raise ValueError("State must contain 'content' and 'embedding' keys.")
    

    key = state["key"]
    # Store the content and embedding in Redis
    # Convert the embedding to a JSON string for storage
    conexionRedis.set(key, json.dumps({"content": state["content"], "embedding": state["embedding"]}))
    
    return state
