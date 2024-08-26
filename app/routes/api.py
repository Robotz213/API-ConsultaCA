from app import app
from app import db

from app import jwt
from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token

from app.models import CaTable, Users
from app.webdriver import DriverLauncher

from datetime import timedelta

# Selenium Imports
from selenium.webdriver.common.by import By

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
def consulta_ca(ca: int):
    
    dbase = CaTable.query.filter(CaTable.cod_ca == ca).first()
    
    json_data = {"ok": "ok"}
    if not dbase:
        
        json_data = get_ca(ca)
    
    response = make_response(jsonify(json_data), 200)
    return response


def get_ca(ca: int) -> dict[str, str]:
    
    driver = DriverLauncher()
    
    driver.get(f"https://consultaca.com/{ca}")
    
    itens_produtos = driver.find_elements(By.TAG_NAME, "p")
    
    dicionario = {}
    
    for item in itens_produtos:
        
        if ":" in item.text:
            data = item.text.replace(": ", ":").split(":")
            
            data_add = data[0].replace("N° do ", "").replace("N° ", "").replace("\n", "")
            
            if any(ignorar == data_add for ignorar in [
                "Deixe sua Avaliação", "Avaliação Geral", "Site", "Registar Dúvida",
                "Marcar como Favorito", "Nome Fantasia", "Cidade/UF"]):
                continue
            
            if data_add == "CA":
                data_add = data_add.replace("CA", "COD_CA")
                
            elif data_add == "Situação":
                data_add = data_add.replace("Situação", "CA")    
            
            info = data[1].replace("\n", "")
            if "vencerá" in info:
                info = info.split("vencerá")[0]
            
            dicionario.update({data_add.lower().replace(" ", "_"): info})
    
    driver.close()
    return dicionario
    
    