from sistema import Sistema
from flask import request, Flask, jsonify

app = Flask(__name__)

system = Sistema("neuro_uff.db", api_mode=True)

@app.route("/login", methods=["POST"])
def login():

    dados = request.json
    login = dados.get("login") # Login = CPF
    senha = dados.get("senha")

    print(f"Tentativa de login: {login}")

    user_logado = system.db.verify_password(login, senha)

    if user_logado:
        pass
        
    # completar o arquivo ainda