from decouple import config

class Config:
    SECRET_KEY_APP = config('SECRET_KEY_APP'),
    SECRET_APP = config('SECRET_APP'),

    URL_1 = config('URL_1')
    URL_2 = config('URL_2')

    OPENAI_API_KEY = config('OPENAI_API_KEY')

    GITHUB_TOKEN_PAT = config('GITHUB_TOKEN_PAT')

    EMBEDDING_MODEL = config('EMBEDDING_MODEL')
    MODEL_TO_USE = config('MODEL_TO_USE')
    MODEL_BEST = config('MODEL_BEST')
    MODEL_SUPER = config('MODEL_SUPER')
    
    LANGCHAIN_API_KEY = config('LANGCHAIN_API_KEY') 

    LANGSMITH_TRACING= config('LANGSMITH_TRACING') 
    LANGSMITH_ENDPOINT= config('LANGSMITH_ENDPOINT') 
    LANGSMITH_API_KEY=config('LANGSMITH_API_KEY')
    LANGSMITH_PROJECT= config('LANGSMITH_PROJECT') 

    CHROMA_PATH = config('CHROMA_PATH') 
    CHROMA_DB = config('CHROMA_DB') 
    CHROMA_COLLECTION = config('CHROMA_COLLECTION') 

    PGSQL_HOST = config('PGSQL_HOST') 
    PGSQL_PORT = config('PGSQL_PORT') 
    PGSQL_USER = config('PGSQL_USER') 
    PGSQL_PASSWORD = config('PGSQL_PASSWORD') 
    PGSQL_DATABASE = config('PGSQL_DATABASE') 

    LANGFUSE_SECRET_KEY = config('LANGFUSE_SECRET_KEY') 
    LANGFUSE_PUBLIC_KEY = config('LANGFUSE_PUBLIC_KEY')
    LANGFUSE_HOST = config('LANGFUSE_HOST')
    

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY_APP = config('SECRET_KEY_APP'),
    SECRET_APP = config('SECRET_APP'),

    URL_1 = config('URL_1')
    URL_2 = config('URL_2')

    OPENAI_API_KEY = config('OPENAI_API_KEY')

    GITHUB_TOKEN_PAT = config('GITHUB_TOKEN_PAT')

    EMBEDDING_MODEL = config('EMBEDDING_MODEL')
    MODEL_TO_USE = config('MODEL_TO_USE')
    MODEL_BEST = config('MODEL_BEST')
    MODEL_SUPER = config('MODEL_SUPER')
    
    LANGCHAIN_API_KEY = config('LANGCHAIN_API_KEY') 

    LANGSMITH_TRACING= config('LANGSMITH_TRACING') 
    LANGSMITH_ENDPOINT= config('LANGSMITH_ENDPOINT') 
    LANGSMITH_API_KEY=config('LANGSMITH_API_KEY')
    LANGSMITH_PROJECT= config('LANGSMITH_PROJECT')     

    CHROMA_PATH = config('CHROMA_PATH') 
    CHROMA_DB = config('CHROMA_DB') 
    CHROMA_COLLECTION = config('CHROMA_COLLECTION') 

    PGSQL_HOST = config('PGSQL_HOST') 
    PGSQL_PORT = config('PGSQL_PORT') 
    PGSQL_USER = config('PGSQL_USER') 
    PGSQL_PASSWORD = config('PGSQL_PASSWORD') 
    PGSQL_DATABASE = config('PGSQL_DATABASE') 

    LANGFUSE_SECRET_KEY = config('LANGFUSE_SECRET_KEY') 
    LANGFUSE_PUBLIC_KEY = config('LANGFUSE_PUBLIC_KEY')
    LANGFUSE_HOST = config('LANGFUSE_HOST')


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY_APP = config('SECRET_KEY_APP'),
    SECRET_APP = config('SECRET_APP'),

    URL_1 = config('URL_1')
    URL_2 = config('URL_2')

    OPENAI_API_KEY = config('OPENAI_API_KEY_PROD')

    GITHUB_TOKEN_PAT = config('GITHUB_TOKEN_PAT')

    EMBEDDING_MODEL = config('EMBEDDING_MODEL')
    MODEL_TO_USE = config('MODEL_TO_USE')
    MODEL_BEST = config('MODEL_BEST')
    MODEL_SUPER = config('MODEL_SUPER')
    
    LANGCHAIN_API_KEY = config('LANGCHAIN_API_KEY') 

    LANGSMITH_TRACING= config('LANGSMITH_TRACING') 
    LANGSMITH_ENDPOINT= config('LANGSMITH_ENDPOINT') 
    LANGSMITH_API_KEY=config('LANGSMITH_API_KEY')
    LANGSMITH_PROJECT= config('LANGSMITH_PROJECT') 
    
    CHROMA_PATH = config('CHROMA_PATH') 
    CHROMA_DB = config('CHROMA_DB') 
    CHROMA_COLLECTION = config('CHROMA_COLLECTION')     
    

    PGSQL_HOST = config('PGSQL_HOST') 
    PGSQL_PORT = config('PGSQL_PORT') 
    PGSQL_USER = config('PGSQL_USER') 
    PGSQL_PASSWORD = config('PGSQL_PASSWORD') 
    PGSQL_DATABASE = config('PGSQL_DATABASE') 

    LANGFUSE_SECRET_KEY = config('LANGFUSE_SECRET_KEY') 
    LANGFUSE_PUBLIC_KEY = config('LANGFUSE_PUBLIC_KEY')
    LANGFUSE_HOST = config('LANGFUSE_HOST')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig

}
