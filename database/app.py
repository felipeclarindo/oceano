from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import *
from time import sleep

# Inicializando a aplicação
app = Flask(__name__)

# Permite que o front end faça requisições, mesmo em dominios diferentes
CORS(app)

# Instanciando o Crud
crud = Crud()

# Criando rota principal 
@app.route('/')
def index():
    return render_template("form.html")

@app.route("/relatos/get", methods=['GET'])
def get_relatos():
    return jsonify(crud.get())

# Criando rota de envio de dados
@app.route("/relatos/post", methods = ['POST'])
def post_relatos():
    print("Recebendo dados do formulario...")
    sleep(1)
    data = request.json
    print(data)
    nome = data["nome"]
    email = data["email"]
    praia = data["praia"]
    descricao = data["descricao"]
    crud.post(nome, email, praia, descricao)
    print("Dados inseridos no banco de dados com sucesso!")
    return jsonify({"message":"Dados inseridos no banco de dados com sucesso!"})


@app.route("/relatos/put", methods=['PUT'])
def put_relatos(id:int, nome:str, email:str, praia:str, descricao:str):
    crud.put(id, nome, email, praia, descricao)
    return jsonify("")

@app.route("/relatos/delete")
def delete_relatos(id:int):
    sucess = crud.delete(id)
    if sucess:
        return jsonify({"message":"Registro deletado com sucesso!"})
    else:
        return jsonify({"message":"Registro não encontrado"})

if __name__ == "__main__":
    # Executa a aplicação
    app.run(debug=True)