import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
SERVER = "db"
DB = os.getenv("POSTGRES_DB")

DEBUG = int(os.getenv("DEBUG", default=0))
SECRET_KEY = os.getenv("SECRET_KEY")
BABEL_DEFAULT_LOCALE = "pt_BR"

SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{SERVER}:5432/{DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
