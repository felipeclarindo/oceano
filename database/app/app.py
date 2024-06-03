from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from database.app.models import *
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
    posted = crud.post(nome, email, praia, descricao)
    if posted["status"] == "succes":
        print("Dados inseridos no banco de dados com sucesso!")
        return jsonify({"message":"Dados inseridos no banco de dados com sucesso!"})
    else:
        return jsonify({"message": "404"})


@app.route("/relatos/put", methods=['PUT'])
def put_relatos(id:int, nome:str, email:str, praia:str, descricao:str):
    update = crud.put(id, nome, email, praia, descricao)
    if update["status"] == "success":
        return jsonify({"message": "Dados enviados com sucesso"})
    else:
        return jsonify({"message": "404"})

@app.route("/relatos/delete")
def delete_relatos(id:int):
    deleted = crud.delete(id)
    if deleted["status"] == "success":
        return jsonify({"message":"Registro deletado com sucesso!"})
    else:
        return jsonify({"message":"Registro não encontrado"})

if __name__ == "__main__":
    # Executa a aplicação
    app.run(debug=True)
    a = post_relatos()
    print(a)