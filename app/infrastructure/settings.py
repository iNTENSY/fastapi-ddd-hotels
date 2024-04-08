import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_FILE)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/jwt/login/")

POSTGRES_USER = os.environ.get("POSTGRES_USER", default='postgres')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", default='postgres')
POSTGRES_DB = os.environ.get("POSTGRES_DB", default='postgres')
DB_HOST = os.environ.get("DB_HOST", default='localhost')
DB_PORT = int(os.environ.get("DB_PORT", default=5432))

TOKEN_LIFETIME = int(os.environ.get('TOKEN_LIFETIME', default=200))
REFRESH_TOKEN_LIFETIME = int(os.environ.get('REFRESH_TOKEN_LIFETIME', default=600))
