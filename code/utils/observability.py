from langfuse._client.get_client import get_client
from langfuse._client.client import Langfuse

import logging
import os

from config import config
config_env = config['default']


langfuse = Langfuse(
    public_key=config_env.LANGFUSE_PUBLIC_KEY,
    secret_key=config_env.LANGFUSE_SECRET_KEY,
    host=config_env.LANGFUSE_HOST,
)

def start_trace(user_id: str, name: str, input_text: str, seed: str, output_text: dict):

    trace_id = langfuse.create_trace_id(seed=seed)

    trace = langfuse.start_as_current_span(
        name="query_trace",
        input=input_text
    )

    # Generate a deterministic ID based on a seed
    # Use the ID with trace context
    with langfuse.start_as_current_span(
        name=name,
        trace_context={"trace_id": trace_id}, input=input_text, output=output_text
    ) as span:
        # Operation will be part of the specific trace
        pass

    return trace

def log_span(trace, name: str, input_data: dict, output_data: dict):

    trace.span(
        name=name,
        input=input_data,
        output=output_data,
    )

def log_error(trace, error_message: str):
    trace.span(
        name="error",
        input={},
        output={"error": error_message},
    )

from datetime import datetime

def CrearArchivoLog():
    # Define la ruta del archivo de registro
    log_dir = os.path.join(os.getcwd(), 'logs')  # Crea un directorio 'logs' en el directorio actual

    log_file = os.path.join(log_dir, f"log_test_rsm{format(datetime.strftime(datetime.today(), '%d_%m_%Y'))}.log")

    # Crea el directorio si no existe
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configura el manejador de archivos
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Añade el manejador al logger
    logger = logging.getLogger('/ingest')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Añade el manejador al logger
    logger = logging.getLogger('/query')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger = logging.getLogger('error')
    logger.addHandler(handler) 
    logger.setLevel(logging.DEBUG)

        # Añade el manejador al logger
    logger = logging.getLogger('test_rsm')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


    # Ahora puedes usar el logger para registrar mensajes
    # logger.debug('Este es un mensaje de depuración')
    logger.info('[COMIENZO DE NUEVOS REGISTROS]')

    # logger.warning('Este es un mensaje de advertencia')
    # logger.error('Este es un mensaje de error')
    # logger.critical('Este es un mensaje crítico')