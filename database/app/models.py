from database.tools.validations import validate_descricao, validate_email, validate_name, validate_praia
from database.tools.utils import EstadoUser, check_user_state, datetoday
from dataclasses import dataclass
from config import connect
import json

@dataclass
class Crud:
    connection = connect()

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
        try:
            self.post_validate(nome, email, praia, descricao)
            if self.user_state == EstadoUser.LIBERADO:
                command = "INSERT INTO relatos (NOME, EMAIL, PRAIA, DESCRICAO, DATA) VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))"
                cursor = self.connection.cursor()
                cursor.execute(command, (nome, email, praia, descricao, datetoday()))
                self.connection.commit()
                cursor.close()
                return {"status": "success"}
            else:
                return {"status": "error", "message": "404"}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
    # Atualizar dados
    def put(self, id:int, nome:str, email:str, praia:str, descricao:str):
        try:
            self.post_validate(nome, email, praia, descricao)
            if self.user_state == EstadoUser.LIBERADO:
                command = "UPDATE relatos SET NOME = :nome, EMAIL = :email, PRAIA = :praia, DESCRICAO = :descricao WHERE ID = :id"
                cursor = self.connection.cursor()
                cursor.execute(command, {'nome':nome, 'email':email, 'praia':praia, 'descricao':descricao, 'id':id})
                cursor.close()
                return {"status": "success"}
            else:
                return {"status": "error", "message": "Dados inválidos."}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    # Atualizar selecionando campo
    def patch(self, id:int, dado:str, novo_dado:str):
        try:
            command = "UPDATE relatos SET :dado = :novo_dado WHERE ID = :id"
            cursor = self.connection.cursor()
            cursor.execute(command, {'dado':dado, 'novo_dado':novo_dado, 'id':id})
            cursor.close()
            return {"status": "success"}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    # Deletar
    def delete(self, id:int):
        try:
            command = f"DELETE FROM relatos WHERE ID = :id"
            cursor = self.connection.cursor()
            cursor.execute(command, {'id':id})
            self.connection.commit()
            cursor.close()
            return {"status": "success"}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    # Obter todos os dados
    def get(self):
        try:
            command = "SELECT * FROM relatos"
            cursor = self.connection.cursor()
            cursor.execute(command)
            usuarios = cursor.fetchall()
            cursor.close()
            return {"status": "success", "message": json.dumps([dict(usuario) for usuario in usuarios])}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
    # Obter dados por ID
    def get_with_id(self, id:int):
        try:
            command = f"SELECT * FROM relatos WHERE ID = :id"
            cursor = self.connection.cursor()
            cursor.execute(command, {'id':id})
            usuario = cursor.fetchone()
            cursor.close()
            return {"status": "success", "message": json.dumps([dict(usuario)])}
        except ValueError as v:
            return {"status": "error", "message": str(v)}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # Finalizando a conexão quando instancia excluida
    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
    pass