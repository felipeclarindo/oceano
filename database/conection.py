from validations import*
from utils import *
import oracledb


# Dados para conexão
username = "rm554547"
userpwd = "130206"
host = "oracle.fiap.com.br"
port = 1521
service_name = "orcl"

# Criando conexão
dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'
connection = oracledb.connect(dsn)
print(connection)

# Criando cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM alunos")
rows = cursor.fetchall()
for row in rows:
    print(row)

print(rows)