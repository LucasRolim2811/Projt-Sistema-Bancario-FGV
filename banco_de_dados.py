"""Descrição: Lê o arquivo CSV e o carrega em um dicionário. Se o arquivo não existir, 
deve retornar um dicionário vazio.


Retorno: Um dicionário no formato {"numero_conta": {"cliente": "Nome", "saldo": 123.45}, ...}. 
O saldo deve ser um float."""

def ler_dicionario(dicionario):
    with open("contas.csv", "r") as arquivo:
        arquivo.write()
    pass

def escrever_no_dicionario(dicionario):
    with open("contas.csv", "w") as arquivo:
        lendo_arquivo = arquivo.read()
        for lines in lendo_arquivo:
            print(lines)
    pass