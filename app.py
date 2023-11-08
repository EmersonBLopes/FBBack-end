from flask import Flask
from flask import request
from flask import Response
from client_controller import Client 
from user import User
import json

app = Flask(__name__)

client = Client()

@app.route("/")
def greeting():
    mensagem = f'<h1>Bem-Vindo a API do ...</h1>\n<p>Para mais informações consulte a documentação</p>'
    return mensagem

@app.route("/users")
def get_users():
    return client.get_users() 

@app.route("/adduser",methods=["POST"])
def append_user():

    json_client = json.loads(request.data)
    print(json_client["name"])
    new_user = User(json_client["ID"],json_client["name"],json_client["last_name"],json_client["email"])

    client.add_user(new_user)
    return "ok"
