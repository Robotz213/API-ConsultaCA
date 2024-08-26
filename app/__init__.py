from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from app.misc.gen_seed import generate_id

app = Flask(__name__)
app.config.from_object("app.default_config")

jwt = JWTManager()
db = SQLAlchemy()
app.secret_key = generate_id()

jwt.init_app(app)
db.init_app(app)

from app.routes import api
