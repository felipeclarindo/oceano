# Validar nome
def validate_name(nome:str) -> bool:
    try:
        nome = nome.strip()
        if nome:
            if len(nome) <= 50:
                if nome.isalpha():
                    return True
                else:
                    raise Exception("O nome deve conter apenas letras!")
            else:
                raise Exception("O tamanho do nome não pode ser maior que 50")
        else:
            raise Exception("O nome não pode ser vazio!")
    except Exception as e:
        print(e)
    return False

# Validar email
def validate_email(email:str) -> bool:
    try:
        email = email.replace(" ", "")
        if email:
            if len(email) <= 40:
                if "@" in email:
                    email_separado = email.split("@")
                    if len(email_separado) == 2:
                        usuario = email_separado[0]
                        dominio = email_separado[1]
                        if "." in dominio:
                            dominio_partes = dominio.split(".")
                            if len(dominio_partes) in (2, 3) and usuario.isalnum():
                                return True
                            else:
                                raise Exception("Não pode ter mais de 2 pontos no dominio.")
                        else:
                            raise Exception("Precisa ter um . após o @.")
                    else:
                        raise Exception('Só pode conter um "@" no email.')
                else:
                    raise Exception('É preciso conter o "@" no seu email.')
            else:
                raise Exception("O email não pode exceder 20 caracteres")
        else:
            raise Exception("O valor não pode ser vazio.")
    except Exception as e:
        print(e)
    return False

# Validar praia
def validate_praia(praia:str) -> bool:
    try:
        praia = praia.replace(" ", "")
        if praia:
            if len(praia) <= 20:
                if praia.isalpha():
                    return True
                else:
                    raise Exception("Deve conter apenas caracteres.")
            else:
                raise Exception("O nome da praia não deve exceder 20 caracteres.")
        else:
            print("O valor não pode ser vazio.")
    except Exception as e:
        print(e)
    return False

# Valida descrição
def validate_descricao(descricao:str) -> bool:
    try:
        descricao = descricao.strip()
        if descricao:
            if len(descricao) <= 200:
                return True
            else:
                print("A descrição não pode exceder 200 caracteres.")
        else:
            raise Exception("O valor não pode ser vazio!")
    except Exception as e:
        print(e)
    return False