from flask import Flask
from client_controller import Client 
from user import User

app = Flask(__name__)

client = Client()

@app.route("/")
def greeting():
    mensagem = f'<h1>Bem-Vindo a API do ...</h1>\n<p>Para mais informações consulte a documentação</p>'
    return mensagem

@app.get("/users")
def get_users():
    return client.get_users() 

@app.route("/appenduser")
def append_user():
    new_user = User(1,"Emerson")
    client.add_user(new_user)
    return "OK"
