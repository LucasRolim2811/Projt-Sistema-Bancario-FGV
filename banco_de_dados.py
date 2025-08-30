import csv

def carregar_contas_de_csv(caminho_arquivo: str = "contas.csv") -> dict:

    """ Faz o acesso ao arquivo csv e lê cada linha contida dentro dele

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está

    Returns:
        dict: Retorna um dicionário possuindo as linhas contidas no arquivo csv dado em caminho_arquivo
    """
    try:
        contas = {}
        with open(caminho_arquivo, "r", encoding='utf-8', newline="") as arquivo_csv:
            acessando_arquivo = csv.DictReader(arquivo_csv)
            for linha in acessando_arquivo:
                numero_conta = linha["numero_conta"]
                linha["saldo"] = float(linha["saldo"]) #Transforma o saldo em float
                contas[numero_conta] = {"nome_cliente": linha["nome_cliente"], "saldo": linha["saldo"]}
        return contas


    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Por favor, digitar um caminho válido.")
        return {}




def salvar_contas_para_csv(caminho_arquivo:str="contas.csv", contas:dict=dict()) -> None:

    """Insere um dicionário dado pelo usuário dentro do banco de dados do csv passado pelo mesmo

    Args:
        caminho_arquivo (str): Argumento que recebe o caminho em que o arquivo csv está
        contas (dict): Dicionário que o usuário quer inserir no banco de dados do arquivo csv
    """
    try:
        with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo_csv:
            colunas = ["numero_conta", "nome_cliente", "saldo"]
            acessar_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            if arquivo_csv.tell() == 0:
                acessar_csv.writeheader()
            for conta, dicionario in contas.items():
                acessar_csv.writerow({"numero_conta": conta, **dicionario})

    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} dado pelo usuário não foi encontrado.")

    else:
        print(f"Dicionário dicionado no banco de dados COM SUCESSO!!!")