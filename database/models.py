from config import *
from validations import *
from utils import *
from dataclasses import dataclass
from datetime import date


@dataclass
class Crud:
    def __init__(self):
        self.connection = connect()
    
    # Finalizando a conexão quando instancia excluida
    def __del__(self):
        self.connection.close()

    # Validação de dados antes do envio
    def post_validate(self, nome:str, email:str, praia:str, descricao:str):
        self.validacoes = [validate_descricao(descricao),
                           validate_name(nome),
                           validate_email(email),
                           validate_praia(praia),
                           validate_descricao(descricao)]
        self.user_state = check_user_state(self.validacoes)

    # Inserir dados no banco de dados
    def post(self, nome:str, email:str, praia:str, descricao:str):
        self.post_validate(nome, email, praia, descricao)
        if self.user_state == EstadoUser.LIBERADO:
            command = "INSERT INTO relatos (NOME, EMAIL, PRAIA, DESCRICAO, DATA) VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))"
            cursor = self.connection.cursor()
            cursor.execute(command, (nome, email, praia, descricao, pegar_data_atual()))
            self.connection.commit()
            cursor.close()
        else:
            return "404"

    # Atualizar dados
    def put(self, id:int, nome:str, email:str, praia:str, descricao:str):
        try:
            self.post_validate(nome, email, praia, descricao)
            if self.user_state == EstadoUser.LIBERADO:
                command = "UPDATE relatos SET NOME = :nome, EMAIL = :email, PRAIA = :praia, DESCRICAO = :descricao WHERE ID = :id"
                cursor = self.connection.cursor()
                cursor.execute(command, {'nome':nome, 'email':email, 'praia':praia, 'descricao':descricao, 'id':id})
                cursor.close()
            else:
                raise ValueError("Dados invalidos")
        except ValueError as v:
            print(v)    
        except Exception as e:
            print(e)

    # Atualizar selecionando campo
    def patch(self, id:int, dado:str, novo_dado:str):
        command = "UPDATE relatos SET :dado = :novo_dado WHERE ID = :id"
        cursor = self.connection.cursor()
        cursor.execute(command, {'dado':dado, 'novo_dado':novo_dado, 'id':id})
        cursor.close()

    # Deletar
    def delete(self, id:int):
        command = f"DELETE FROM relatos WHERE ID = :id"
        cursor = self.connection.cursor()
        cursor.execute(command, {'id':id})
        self.connection.commit()
        cursor.close()

    # Obter todos os dados
    def get(self):
        command = "SELECT * FROM relatos"
        cursor = self.connection.cursor()
        cursor.execute(command)
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    # Obter dados por ID
    def get_with_id(self, id:int):
        command = f"SELECT * FROM relatos WHERE ID = :id"
        cursor = self.connection.cursor()
        cursor.execute(command, {'id':id})
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

if __name__ == "__main__":
    pass