import time
import logging
def time_execution(fn):
    def wrapper(state):
        start = time.time() 
        result = fn(state)
        elapsed = time.time() - start

        logger = logging.getLogger("test_rsm")
        logger.info(f"[{fn.__name__}] Tiempo de ejecución: {elapsed:.2f}s")
        return result
    return wrapper
