"""Descrição: Lê o arquivo CSV e o carrega em um dicionário. Se o arquivo não existir, 
deve retornar um dicionário vazio.


Retorno: Um dicionário no formato {"numero_conta": {"cliente": "Nome", "saldo": 123.45}, ...}. 
O saldo deve ser um float."""

import csv

def carregar_contas_de_csv(caminho_arquivo: str) -> dict:

    """ Faz o acesso ao arquivo csv e lê cada linha contida dentro dele

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está

    Returns:
        dict: Retorna um dicionário possuindo as linhas contidas no arquivo csv dado em caminho_arquivo
    """
    try:
        with open(caminho_arquivo, "r",encoding='utf-8') as arquivo_csv:
            acessando_arquivo = csv.DictReader(arquivo_csv)
            for lines in acessando_arquivo:
                print(lines)
        return acessando_arquivo
    
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Por favor, digitar um caminho válido.")

def salvar_contas_para_csv(caminho_arquivo:str="contas.csv", contas:dict=dict()) -> None:

    """Insere um dicionário dado pelo usuário dentro do banco de dados do csv passado pelo mesmo

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está
        contas (dict): Dicionário que o usuário quer inserir no banco de dados do arquivo csv
    """
    try:
        with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo_csv:
            colunas = ["nome_cliente", "saldo"]
            acessar_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            acessar_csv.writeheader()
            acessar_csv.writerow(contas)

    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} dado pelo usuário não foi encontrado.")

    else:
        print(f"Dicionário dicionado no banco de dados COM SUCESSO!!!")


# Driver code


carregar_contas_de_csv("contas.csv")
salvar_contas_para_csv("contas.csv", {"nome_cliente": "Rafael", "saldo": 0})
