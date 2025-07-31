from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY_TEST'),
    OPENAI_API_KEY = config('OPENAI_API_KEY')
    REDIS_URL = config('REDIS_URL')
    REDIS_PORT = config('REDIS_PORT')
    REDIS_USERNAME = config('REDIS_USERNAME')
    REDIS_PASSWORD = config('REDIS_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = config('SECRET_KEY_TEST'),
    OPENAI_API_KEY = config('OPENAI_API_KEY')
    REDIS_URL = config('REDIS_URL')
    REDIS_PORT = config('REDIS_PORT')
    REDIS_USERNAME = config('REDIS_USERNAME')
    REDIS_PASSWORD = config('REDIS_PASSWORD')

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "nada",
    OPENAI_API_KEY = config('OPENAI_API_KEY_PROD')
    REDIS_URL = config('REDIS_URL')
    REDIS_PORT = config('REDIS_PORT')
    REDIS_USERNAME = config('REDIS_USERNAME')
    REDIS_PASSWORD = config('REDIS_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig

}

# import os

# THINK_PYTHON_URL = "https://allendowney.github.io/ThinkPython/index.html"
# PEP8_URL = "https://peps.python.org/pep-0008/"
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
# LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
# LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")