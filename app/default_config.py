from dotenv import dotenv_values
from uuid import uuid4
import os

host_db = dotenv_values()['host']
login_db = dotenv_values()['login']
passwd_db = dotenv_values()['password']
database_name = dotenv_values()['database']

## PARAMETROS PARA O APP FLASK
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_COOKIE_HTTPONLY = False
SQLALCHEMY_DATABASE_URI = f"mysql://{login_db}:{passwd_db}@{host_db}/{database_name}"
SESSION_COOKIE_SECURE = True
PREFERRED_URL_SCHEME = "https"
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "CHROMEDRIVER_PATH")
JWT_SECRET_KEY = str(uuid4())
SRC_IMG_PATH = os.path.join(os.getcwd(), "app", "src", "assets", "img")


for paths in [CHROMEDRIVER_PATH]:
    os.makedirs(paths, exist_ok=True)