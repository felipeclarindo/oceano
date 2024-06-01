import oracledb

def connect():
    try:
        # Dados para conexão
        username = "rm554547"
        userpwd = "130206"
        host = "oracle.fiap.com.br"
        port = 1521
        service_name = "ORCL"

        # Criando conexão
        dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'
        connection = oracledb.connect(dsn)
        print("Conexão Bem Sucedida!")
        return connection
    except Exception:
        print("Falha na conexão!")
    return False