import os
from uuid import uuid4

from dotenv import dotenv_values

"""
This module sets up the default configuration for a Flask application.

Configuration parameters:
- SQLALCHEMY_TRACK_MODIFICATIONS: Disables SQLAlchemy modification tracking.
- SESSION_COOKIE_HTTPONLY: Sets the HttpOnly flag for session cookies.
- SQLALCHEMY_DATABASE_URI: The database URI for SQLAlchemy, constructed using environment variables.
- SESSION_COOKIE_SECURE: Ensures session cookies are only sent over HTTPS.
- PREFERRED_URL_SCHEME: Sets the preferred URL scheme to HTTPS.
- CHROMEDRIVER_PATH: Path to the ChromeDriver executable.
- JWT_SECRET_KEY: A randomly generated secret key for JWT.
- SRC_IMG_PATH: Path to the source images directory.

Environment variables (loaded from .env file):
- host: Database host.
- login: Database login username.
- password: Database login password.
- database: Database name.

Directories:
- CHROMEDRIVER_PATH: Ensures the ChromeDriver path directory exists.
"""

host_db = dotenv_values()["host"]
login_db = dotenv_values()["login"]
passwd_db = dotenv_values()["password"]
database_name = dotenv_values()["database"]

# PARAMETROS PARA O APP FLASK
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
