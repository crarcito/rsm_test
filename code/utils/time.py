import time
import logging as logger
def time_execution(fn):
    def wrapper(state):
        start = time.time()
        result = fn(state)
        elapsed = time.time() - start
        logger.info(f"[{fn.__name__}] Tiempo de ejecución: {elapsed:.2f}s")
        return result
    return wrapper
