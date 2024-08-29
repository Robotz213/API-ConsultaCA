from app import db
from app import app
from app import limiter

from app import jwt
from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token

from app.models import CaTable, Users
from app.webdriver import DriverLauncher

from datetime import timedelta

# Selenium Imports
from selenium.webdriver.common.by import By

import unicodedata
from datetime import datetime

@app.route("/login", methods = ["POST"])
def login():
    
    ## Sistema de autenticação JWT
    user = request.json.get("username", None)
    password = request.json.get("password", None)
    
    ## Verifica se no request.json tem esses dois parâmetros
    if user and password:
        
        ## Verifica se o usuário informado está no database
        usuario_logado = Users.query.filter(Users.username == user).first()
        if usuario_logado:
            
            ## Verifica a senha
            checkpw = usuario_logado.converte_senha(password)
            if checkpw:
                
                ## Define o tempo de expiração do Token JWT e retorna ele
                expires = timedelta(hours=2)
                access_token = create_access_token(identity=user, expires_delta=expires)
                return jsonify(access_token=access_token), 200
            
    return jsonify({"error": "require auth"}), 401

@app.route("/consulta_ca/<ca>", methods = ["GET"])
@jwt_required()
@limiter.limit("250/minute")
def consulta_ca(ca: int):
    
    dbase = CaTable.query.filter(CaTable.cod_ca == int(ca)).first()
    json_data = {}
    if not dbase:
        
        get_data = get_ca(ca)
        if len(get_data) > 0:
        
            redata = {}
            for column in CaTable.__table__.columns:
                
                redata.update({column.name: get_data.get(column.name)})
                
                if column.name == "validade":
                    dataformat = datetime.strptime(get_data.get(column.name), "%d/%m/%Y")
                    redata.update({column.name: dataformat})
                    
            add_epi = CaTable(**redata)
            db.session.add(add_epi)
            db.session.commit()
            json_data = redata
        
    if dbase:
        
        json_data = {}
        for column in CaTable.__table__.columns:
            
            json_data.update({column.name: getattr(dbase, column.name)})
    
    response = make_response(jsonify(json_data), 200)
    if len(json_data) == 0:
        response = make_response(jsonify({"error": "CA NÃO ENCONTRADA!"}), 404)
        
    return response


def get_ca(ca: int) -> dict[str, str]:
    
    driver = DriverLauncher()
    
    driver.get(f"https://consultaca.com/{ca}")
    
    dicionario = {}
    
    if driver.current_url != 'https://consultaca.com/':
    
        itens_produtos = driver.find_elements(By.TAG_NAME, "p")
        
        
        
        nome_epi = driver.find_element(By.CSS_SELECTOR, '#titulo-equipamento > div > h1').text
        tipo_epi = driver.find_element(By.CSS_SELECTOR, '#titulo-equipamento > div > span').text
        
        dicionario.update({'nome_epi': nome_epi})
        dicionario.update({'tipo_epi': tipo_epi})
        
        for item in itens_produtos:
            
            if ":" in item.text:
                data = item.text.replace(": ", ":").split(":")
                
                data_add = data[0].replace("N° do ", "").replace("N° ", "").replace("\n", "")
                
                if any(ignorar == data_add for ignorar in [
                    "Deixe sua Avaliação", "Avaliação Geral", "Site", "Registar Dúvida",
                    "Marcar como Favorito", "Nome Fantasia", "Cidade/UF"]):
                    continue
                
                info = data[1].replace("\n", "")
                if "vencerá" in info:
                    info = info.split("vencerá")[0]
                    
                if data_add == "CA":
                    data_add = data_add.replace("CA", "COD_CA")
                    info = int(info)
                    
                elif data_add == "Situação":
                    data_add = data_add.replace("Situação", "CA")   
                
                data_add = "".join([c for c in unicodedata.normalize(
                    'NFKD', data_add) if not unicodedata.combining(c)])
                
                dicionario.update({data_add.lower().replace(" ", "_"): info})
    
    driver.close()
    return dicionario
    
    