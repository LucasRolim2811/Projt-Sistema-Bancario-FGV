import banco_de_dados

class Erro_No_Banco(Exception):
    """Verifica se o numero da conta existe"""
class Conta_Inexistente(Erro_No_Banco):
    """Numero da conta(numero_conta) não existe no banco de dados"""
class Saldo_Insuficiente(Erro_No_Banco):
    """Saldo inferior ao requisitado. Impossível realizar operação"""

def criar_conta(numero_conta: str, nome_cliente: str) -> tuple[int, dict]:
    """Vai criar uma conta dentro do csv de contas.csv

    Args:
        numero_conta (str): Vai colocar o código da conta que se deseja criar
        nome_cliente (str): Nome do cliente que fará a conta

    Returns:
        tuple[int, dict]: Retorna uma tupla com o numero da conta e um dicionário com o nome e saldo do cliente
    """
    dicionarios = banco_de_dados.carregar_contas_de_csv()
    if numero_conta in dicionarios.keys():
        print("Esse código já existe!!")
    elif numero_conta not in dicionarios.keys():
        banco_de_dados.salvar_contas_para_csv(contas={"numero_conta": numero_conta,"nome_cliente": nome_cliente, "saldo": 0}) #Insere os dados no csv
        return (numero_conta, {"nome_cliente": nome_cliente, "saldo": 0})
    

def depositar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Deposita um uma valor dado no saldo da conta especificada

    Args:
        numero_conta (str): Código da conta que se deseja fazer o depósito
        valor (float): Valor que se deseja depositar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    """
    dicionarios = banco_de_dados.carregar_contas_de_csv()
    if numero_conta in dicionarios.keys():
        print("-" * 30)
        print("Sua conta existe!!")
        dicionarios[numero_conta]["saldo"] = banco_de_dados.salvar_contas_para_csv(valor)
    elif numero_conta not in dicionarios.keys():
        print("Tentativa de depósito falhou. Por favor, digitar uma conta válida")


def sacar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Faz um saque na conta especificada. Subtrai o valor diretamente do saldo da conta

    Args:
        numero_conta (str): Código da conta que se deseja fazer o saque
        valor (float): Valor que se deseja sacar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    """
    dicionarios = banco_de_dados.carregar_contas_de_csv()
    try:
        saldo_disponivel = dicionarios[numero_conta]["saldo"]
        saldo_disponivel = saldo_disponivel - valor
        banco_de_dados.salvar_contas_para_csv(contas=dicionarios)

        
    except Conta_Inexistente:
        print("Tal conta é inválida! Tente uma válida")
    
    else:
        print("deu bom")

def consultar_saldo(numero_conta: str) -> float | None:
    """Verifica o saldo da conta informada

    Args:
        numero_conta (str): Código da conta que será acessada

    Returns:
        float | None: Retorna o saldo(em float) se a conta existir ou None caso contrário
    """
    pass

def somar_saldos_gerais( ) -> float:
    """Soma todos os saldos das contas informadas

    Returns:
        float: Retorna a soma de todas as contas cadastradas
    """
    pass

def identificar_cliente_mais_rico( ) -> dict | None:
    """Verifica qual cliente possui maior saldo na conta

    Returns:
        dict | None: Retorna todos os dados do cliente com maior saldo. None caso não haja contas no banco
    """
    pass


def somar_saldos_em_lote(**kwargs) -> int:
    """Soma valores aos saldos de múltiplas contas de uma vez. As chaves dos kwargs serão os números das contas 
    e os valores serão os montantes a serem adicionados.

    Returns:
        int: A quantidade de contas que foram atualizadas com sucesso. Contas inexistentes ou valores negativos 
        devem ser ignorados
    """
    pass

def subtrair_saldos_em_lote(**kwargs) -> int:
    """Subtrai valores dos saldos de múltiplas contas de uma vez. Falha para uma conta específica se o saldo 
    for insuficiente, mas continua para as outras.

    Returns:
        int: A quantidade de contas que tiveram o saldo removido com sucesso. Contas inexistentes,
        valores negativos ou tentativas de saque maiores que o saldo devem ser ignoradas.
    """
    pass

def realizar_transferencia(conta_origem: str, conta_destino: str, valor: float) -> tuple[bool, str]:
    """Realiza uma transferência entre duas contas. Se não for possível realizar a operação, seja por 
    falta de saldo ou pela outra conta não existir, o retorno deve indicar a falha.

    Args:
        conta_origem (str): Código da conta da onde deseja transferir
        conta_destino (str): Código da conta que se deseja receber a transferência
        valor (float): Valor que se deseja transferir

    Returns:
        tuple[bool, str]: Tupla (sucesso, mensagem). Ex: (True, "Transferência realizada com sucesso.") 
        ou (False, "Saldo insuficiente").
    """
    pass

