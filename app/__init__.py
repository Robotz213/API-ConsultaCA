from flask import Flask
from flask_limiter import Limiter
from flask_sqlalchemy import SQLAlchemy
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager, get_jwt_identity

from app.misc.gen_seed import generate_id

app = Flask(__name__)
app.config.from_object("app.default_config")

jwt = JWTManager()
db = SQLAlchemy()

limiter = Limiter(
    key_func=lambda: get_jwt_identity or get_remote_address,  # Limitação por token JWT ou IP
    default_limits=["5 per minute"],  # Limite de 5 requisições por minuto
    storage_uri="memory://",
    storage_options={"socket_connect_timeout": 30},
    strategy="fixed-window", # or "moving-window"
)

app.secret_key = generate_id()

jwt.init_app(app)
db.init_app(app)
limiter.init_app(app)


from app.routes import api
