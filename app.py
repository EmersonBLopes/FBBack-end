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
    requeststr = str(request.data)
    new_user = json.loads(requeststr)
    print(requeststr)
    
    return "ok"
