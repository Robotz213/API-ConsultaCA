from app import db

from pytz import timezone
from datetime import datetime


class CaTable(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ca = db.Column(db.String(length=64))
    cod_ca = db.Column(db.Integer)
    nome_epi = db.Column(db.String(length=64), unique=True)
    tipo_epi = db.Column(db.String(length=64))
    validade = db.Column(db.DateTime, default=datetime.now(timezone('Etc/GMT+4')))
    aprovado_para = db.Column(db.Text)
    cnpj_do_laboratorio = db.Column(db.Text)
    cnpj_importador = db.Column(db.Text)
    laudo = db.Column(db.Text)
    marcacao = db.Column(db.Text)
    natureza = db.Column(db.Text)
    processo = db.Column(db.Text)
    razao_social = db.Column(db.Text)
    razao_social_importador = db.Column(db.Text)
    referencias = db.Column(db.Text)
