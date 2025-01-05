from importlib import import_module

from flask import Flask
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

from app.misc.gen_seed import generate_id

"""
This module initializes the Flask application along with its extensions and configurations.

Modules and Packages Imported:
- importlib.import_module: Dynamically imports a module.
- flask: Flask framework for creating web applications.
- flask_jwt_extended: JWT (JSON Web Token) extension for Flask.
- flask_limiter: Rate limiting extension for Flask.
- flask_sqlalchemy: SQLAlchemy extension for Flask.
- app.misc.gen_seed: Custom module to generate unique IDs.

Variables:
- app: The Flask application instance.
- jwt: The JWTManager instance for handling JWTs.
- db: The SQLAlchemy instance for database interactions.
- limiter: The Limiter instance for rate limiting.

Configurations:
- app.config.from_object("app.default_config"): Loads default configurations from the specified module.
- app.secret_key: Sets the secret key for the application using a generated unique ID.

Extensions Initialization:
- jwt.init_app(app): Initializes the JWTManager with the Flask app.
- db.init_app(app): Initializes the SQLAlchemy with the Flask app.
- limiter.init_app(app): Initializes the Limiter with the Flask app.

Rate Limiting:
- key_func: Determines the key for rate limiting using JWT identity or remote address.
- default_limits: Sets the default rate limit to 5 requests per minute.
- storage_uri: Specifies the storage backend for rate limiting.
- storage_options: Additional options for the storage backend.
- strategy: The rate limiting strategy used (fixed-window or moving-window).

Routes:
- Dynamically imports the API routes module using import_module("app.routes.api").
"""


app = Flask(__name__)
app.config.from_object("app.default_config")

jwt = JWTManager()
db = SQLAlchemy()

limiter = Limiter(
    key_func=lambda: get_jwt_identity
    or get_remote_address,  # Limitação por token JWT ou IP
    default_limits=["5 per minute"],  # Limite de 5 requisições por minuto
    storage_uri="memory://",
    storage_options={"socket_connect_timeout": 30},
    strategy="fixed-window",  # or "moving-window"
)

app.secret_key = generate_id()

jwt.init_app(app)
db.init_app(app)
limiter.init_app(app)

import_module("app.routes.api")
