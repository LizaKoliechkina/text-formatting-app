import os

PROJECT_NAME = 'text formatting app'

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', 5432))
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

SQLALCHEMY_DB_URI = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)
