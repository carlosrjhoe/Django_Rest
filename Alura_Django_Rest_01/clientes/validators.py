import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    """Verificar se o cpf é válido (123.123.123-12))"""
    cpf = CPF()
    return cpf.validate(numero_cpf)
    
def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verificar se o celular é válido (81 91234-1234))"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta