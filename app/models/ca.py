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


{
    "Aprovado Para": " PROTEÇÃO DO CRÂNIO E FACE DO USUÁRIO CONTRA RISCOS PROVENIENTES DE FONTES GERADORAS DE CALOR NOS TRABALHOS DE COMBATE A INCÊNDIO.",
    "Avaliação Geral": "",
    "CNPJ Importador": " 45.655.461/0001-30",
    "CNPJ do Laboratório": " 10.000.000/0000-10",
    "Cidade/UF": " DIADEMA/SP",
    "Cor": " Diversas.",
    "Deixe sua Avaliação": "",
    "Feito com por SafetyTec Tecnologia e Inovação em Seg. do Trabalho LTDA. - CNPJ": "14.957.619/0001-01",
    "Marcar como Favorito": "",
    "Marcação": " Parte interna do casco.",
    "Natureza": " Importado",
    "Nome Fantasia": " MSA",
    "CA": " 13037",
    "Processo": " 19980212903202378",
    "do Laudo": " SEI nº FF MSA 17",
    "Razão Social": " SAFETY EQUIPMENT INSTITUTE",
    "Razão Social Importador": " MSA DO BRASIL EQUIP E INSTRUMENTOS DE SEGURANCA LTDA",
    "Referências": " CAPACETE PARA BOMBEIROS MSA CAIRNS 660",
    "Registar Dúvida": "",
    "Site": " http",
    "Situação": " VÁLIDO",
    "Validade": " 20/11/2028"
}