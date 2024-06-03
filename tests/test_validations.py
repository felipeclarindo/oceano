import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.tools.validations import *

# Testes de validação de email
def test_validate_email_passeds():
    assert validate_email("aaa@gmail.com") == True
    assert validate_email("aaa@gmail.com.br") == True
    assert validate_email("aaaaa@gmail.com") == True
    assert validate_email("    aaa@gmail.com    ") == True

def test_validate_email_fails():
    assert validate_email("aaaaaa") == False
    assert validate_email("@aa@aaaa") == False
    assert validate_email("aaa@a.a.aa.a") == False
    assert validate_email("a.aaa@") == False
    assert validate_email("aa@gmail.m@com") == False
    assert validate_email("aa@gmail.m@comgmaijda1gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1") == False
    assert validate_email("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com") == False
    assert validate_email("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com.br") == False

# Testes de validação de nome de praia
def test_validate_praia_passeds():
    assert validate_praia("jamanbaia") == True
    assert validate_praia("miama") == True
    assert validate_praia("    praiaaa    ") == True

def test_validate_praia_fails():
    assert validate_praia("") == False
    assert validate_praia("1231aa") == False
    assert validate_praia("   241asdaada21") == False
    assert validate_praia("@gmaijda1!") == False
    assert validate_praia("@gmaijda1!gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1gmaijda1") == False

# Testes validação descricao
def test_validate_descricao_passeds():
    assert validate_descricao("aaaadkaodki!4ki") == True
    assert validate_descricao("             94914ijaia pero ´13[2]") == True
    assert validate_descricao("essa é a descrição e ela é valida !!!") == True
    assert validate_descricao("adaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaaaadaadaadaad") == True
    assert validate_descricao("                 adaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaaaadaadaadaad                    ") == True

def test_validate_descricao_fails():
    assert validate_descricao("") == False
    assert validate_descricao("daadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaaaadaadaadaad2adaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaaaadaadaadaad2") == False
    assert validate_descricao("            aadaadaadaaadaadaadaadaadaadaadaadaadaadaadaadaadaadaa231daadaadaadaadaadaadaadaadaadaadaaaadaadaadaad2adaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaaaadaadaada     ") == False

# Testes validação nome
def test_validate_nome_passeds():
    assert validate_name("felipe") == True
    assert validate_name("   felipe    ") == True
    assert validate_name("   Felipe    ") == True
    assert validate_name("Feliuoe") == True
    assert validate_name("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
    assert validate_name("    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa     ") == True

def test_validate_nome_fails():
    assert validate_name("123") == False
    assert validate_name(   "123"  ) == False
    assert validate_name("felipe1234") == False
    assert validate_name("    felipe1234"   ) == False
    assert validate_name("felaoipelafelaoipelafelaoipelafelaoipelafelaoipelaa") == False
    assert validate_name("                 felaoipelafelaoipelafelaoipelafelaoipelafelaoipelaa             ") == False

    
    