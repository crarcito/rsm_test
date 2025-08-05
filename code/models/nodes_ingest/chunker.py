from langchain.text_splitter import RecursiveCharacterTextSplitter

from datetime import datetime
from utils.observability import start_trace, log_span, log_error
import utils.time as tiempo, logging as logger

@tiempo.time_execution
def chunk_text(state, chunk_size=512):
    """Chunk the text content into smaller pieces."""

    #     splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    #     chunks = splitter.split_documents(docs)

    logger.info(f"start chunk_state sin decorador")

    text = state["text"]
    if not text:
        raise ValueError("No text content to chunk.")
    
    # # Split the text into chunks of specified size
    # # This is a simple split; you might want to use a more sophisticated method
    # # such as sentence or paragraph splitting to avoid breaking words.
    # # Here, we just split by character count.
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, chunk_overlap=0)
    # chunks = text_splitter.split_documents(text)

    if not chunks:
        raise ValueError("No chunks created from the text content.")
    
    # Store the chunks in the state
    state["chunks"] = chunks
    
    return state