from datetime import datetime

from pytz import timezone

from app import db


class CaTable(db.Model):
    """
    CaTable represents a table in the database for storing information about CA (Certificate of Approval).

    Attributes:
        id (int): Primary key, unique identifier for each record.
        ca (str): CA number.
        cod_ca (int): CA code.
        nome_epi (str): Name of the EPI (Personal Protective Equipment), must be unique.
        tipo_epi (str): Type of the EPI.
        validade (datetime): Expiration date of the CA, defaults to the current date and time in the GMT+4 timezone.
        aprovado_para (str): Approved for specific uses.
        cnpj_do_laboratorio (str): CNPJ of the laboratory.
        cnpj_importador (str): CNPJ of the importer.
        laudo (str): Report or certificate.
        marcacao (str): Marking information.
        natureza (str): Nature of the CA.
        processo (str): Process information.
        razao_social (str): Corporate name of the company.
        razao_social_importador (str): Corporate name of the importer.
        referencias (str): References related to the CA.
    """

    id = db.Column(db.Integer, primary_key=True, unique=True)
    ca = db.Column(db.String(length=64))
    cod_ca = db.Column(db.Integer)
    nome_epi = db.Column(db.String(length=64), unique=True)
    tipo_epi = db.Column(db.String(length=64))
    validade = db.Column(db.DateTime, default=datetime.now(timezone("Etc/GMT+4")))
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
