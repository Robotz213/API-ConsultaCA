from app import db

from pytz import timezone
from datetime import datetime


class CaTable(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ca = db.Column(db.String(length=64))
    cod_ca = db.Column(db.Integer)
    nome_epi = db.Column(db.String(length=64), unique=True)
    tipo_epi = db.Column(db.String(length=64))
    valor_unitario = db.Column(db.Float)
    vencimento = db.Column(db.DateTime, default=datetime.now(timezone('Etc/GMT+4')))
