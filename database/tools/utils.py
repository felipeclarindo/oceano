from datetime import date
from enum import StrEnum

class EstadoUser(StrEnum):
    LIBERADO = "liberado"
    BLOQUEADO = "bloqueado"
    
def datetoday() -> str:
    data = date.today()
    return data.strftime("%Y/%m/%d")

def check_user_state(validacoes):
    for validacao in validacoes:
        if not validacao:
            return EstadoUser.BLOQUEADO
    else:
        return EstadoUser.LIBERADO