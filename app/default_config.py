from app.misc.gen_seed import generate_id

from dotenv import dotenv_values
import os

login_db = dotenv_values()['login']
passwd_db = dotenv_values()['password']
host_db = dotenv_values()['host']
database_name = dotenv_values()['database']

## PARAMETROS PARA O APP FLASK
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "CHROMEDRIVER_PATH")
SQLALCHEMY_DATABASE_URI = f"mysql://{login_db}:{passwd_db}@{host_db}/{database_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False   
PREFERRED_URL_SCHEME = "https"
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = True
SRC_IMG_PATH = os.path.join(os.getcwd(), "app", "src", "assets", "img")
JWT_SECRET_KEY = generate_id()


for paths in [CHROMEDRIVER_PATH]:
    os.makedirs(paths, exist_ok=True)