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

{
    "aprovado_para": "PROTEÇÃO DO CRÂNIO E FACE DO USUÁRIO CONTRA RISCOS PROVENIENTES DE FONTES GERADORAS DE CALOR NOS TRABALHOS DE COMBATE A INCÊNDIO.",
    "ca": "VÁLIDO",
    "cnpj_do_laboratório": "10.000.000/0000-10",
    "cnpj_importador": "45.655.461/0001-30",
    "cod_ca": "13037",
    "cor": "Diversas.",
    "deixe_suaavaliação": "",
    "feito_com_por_safetytec_tecnologia_e_inovação_em_seg._do_trabalho_ltda._-_cnpj": "14.957.619/0001-01",
    "laudo": "SEI nº FF MSA 17",
    "marcar_comofavorito": "",
    "marcação": "Parte interna do casco.",
    "natureza": "Importado",
    "processo": "19980212903202378",
    "razão_social": "SAFETY EQUIPMENT INSTITUTE",
    "razão_social_importador": "MSA DO BRASIL EQUIP E INSTRUMENTOS DE SEGURANCA LTDA",
    "referências": "CAPACETE PARA BOMBEIROS MSA CAIRNS 660",
    "registardúvida": "",
    "validade": "20/11/2028"
}