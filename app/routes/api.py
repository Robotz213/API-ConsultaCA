from app import app
from app import db

from app import jwt
from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token

from app.models import CaTable, Users
from app.webdriver import DriverLauncher

from datetime import timedelta

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
    
    if not dbase:
        
        driver = DriverLauncher()
        driver.close()
    
    response = make_response(jsonify({"ok": "ok"}), 200)
    return response
