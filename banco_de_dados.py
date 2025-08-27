"""Descrição: Lê o arquivo CSV e o carrega em um dicionário. Se o arquivo não existir, 
deve retornar um dicionário vazio.


Retorno: Um dicionário no formato {"numero_conta": {"cliente": "Nome", "saldo": 123.45}, ...}. 
O saldo deve ser um float."""

import csv

def carregar_contas_de_csv(caminho_arquivo: str) -> dict: #Está funcionando bem
    """ Faz o acesso ao arquivo csv e lê cada linha contida dentro dele

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está

    Returns:
        dict: Retorna um dicionário possuindo as linhas contidas no arquivo csv dado em caminho_arquivo
    """
    with open(caminho_arquivo, "r",encoding='utf-8') as arquivo_csv:
        acessando_arquivo = csv.reader(arquivo_csv)
        for lines in acessando_arquivo:
            print(lines)
    return

def salvar_contas_para_csv(caminho_arquivo:str, contas:dict) -> None: #Precisa verificar se está salvando o arquivo no final
    """Insere um dicionário dado pelo usuário dentro do banco de dados do csv passado pelo mesmo

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está
        contas (dict): Dicionário que o usuário quer inserir no banco de dados do arquivo csv
    """
    try:
        with open(caminho_arquivo, "w", encoding='utf-8') as arquivo_csv:
            acessar_csv = csv.writer(arquivo_csv)
            escrever_csv = acessar_csv.writerow(contas)
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} dado pelo usuário não foi encontrado.")
    else:
        print("Arquivo acessado COM SUCESSO!!!")


# Driver code

carregar_contas_de_csv("contas.csv")
salvar_contas_para_csv("contas.csv", {"nome": "rafael", "idade":22, "hobbie": "basquete"})
salvar_contas_para_csv("contas.csv", {"nome": "lucas", "idade":20})
carregar_contas_de_csv("contas.csv")
