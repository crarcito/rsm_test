import time
import logging

def time_execution(fn):
    def wrapper(stateWrapper):
        start = time.time() 
        result = fn(stateWrapper)
        elapsed = time.time() - start

                # Crear un manejador de salida estándar
        logger = logging.getLogger("test_rsm")

        # console = logging.StreamHandler(sys.stdout)
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # console.setFormatter(formatter)
        # console.setLevel(logging.DEBUG)
        # logger.addHandler(console)


        msg = f"[{fn.__name__}] Tiempo de ejecución2: {elapsed:.2f}s"
        logger.info(msg)

        print("INFO: " + str(msg))
        
        return result
    return wrapper


