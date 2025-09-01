import banco_de_dados
import doctest
#########################################################################################

class Erro_No_Banco(Exception):
    """Relata que houve erro no sistema"""
class Conta_Inexistente(Erro_No_Banco):
    """Numero da conta(numero_conta) não existe no banco de dados"""
class Conta_nao_numero(Erro_No_Banco):
    """A conta adicionada não é um número"""
class Saldo_Insuficiente(Erro_No_Banco):
    """Saldo inferior ao requisitado. Impossível realizar operação"""

def conta_no_padrao(numero_conta:str) -> tuple[bool, str]:
    """Verifica se o numero da conta é menor que 9999 e se possui 4 caracteres

    Args:
        numero_conta (str): String correspondente ao numero da conta que deve ser analisado

    Returns:
        tuple[bool, str]: Tupla respondendo se o número da conta satisfaz as condições(bool) e com uma mensagem de feedback(str)
    
    >>> conta_no_padrao("0023")
    (True, 'Sua conta está no padrão do banco de dados')
    >>> conta_no_padrao("Eu amo a emap")
    (False, 'Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido')
    """
    try:
        conta = int(numero_conta)
        if conta > 9999 or len(numero_conta) > 4:
            return (False, "Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido")
        else:
            return (True, "Sua conta está no padrão do banco de dados")
    except ValueError:
        return (False, "Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido")

def criar_conta(numero_conta: str, nome_cliente: str) -> tuple[int, dict]:
    """Vai criar uma conta dentro do csv de contas.csv

    Args:
        numero_conta (str): Vai colocar o código da conta que se deseja criar
        nome_cliente (str): Nome do cliente que fará a conta

    Returns:
        tuple[int, dict]: Retorna uma tupla com o numero da conta e um dicionário com o nome e saldo do cliente
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    if conta_no_padrao()[0]:
        if numero_conta not in dicionario_do_banco:
            dicionario_do_banco[numero_conta] = {"nome_cliente": nome_cliente,"saldo": 0}
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            conta_criada = banco_de_dados.carregar_contas_de_csv()[numero_conta]
            return (numero_conta, conta_criada)
        else:
            print("Esta conta já esxiste! Por favor, senhor gerente, colocar uma conta ainda não criada!")
    else:
        return conta_no_padrao()[1]
        
    

def depositar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Deposita um valor dado no saldo da conta especificada

    Args:
        numero_conta (str): Código da conta que se deseja fazer o depósito
        valor (float): Valor que se deseja depositar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    situacao_do_deposito = tuple()
    if conta_no_padrao[0]:
        if numero_conta in dicionario_do_banco and valor > 0:
            dicionario_do_banco[numero_conta]["saldo"] += valor 
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            situacao_do_deposito = (True, "Depósito realizado com sucesso!")
        elif valor < 0:
            situacao_do_deposito = (False, "Adicionar um valor MAIOR QUE ZERO!")
        else:
            situacao_do_deposito = (False, "Conta inexistente!")
        return situacao_do_deposito
    else:
        return conta_no_padrao[1]


def sacar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Faz um saque na conta especificada. Subtrai o valor diretamente do saldo da conta

    Args:
        numero_conta (str): Código da conta que se deseja fazer o saque
        valor (float): Valor que se deseja sacar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    situacao_do_saque = ()
    if conta_no_padrao()[0]:
        if numero_conta in dicionario_do_banco and valor > 0:
            dicionario_do_banco[numero_conta]["saldo"] -= valor
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            situacao_do_saque = (True, "Valor sacado com sucesso")
        elif valor < 0:
            situacao_do_saque = (False, "Adicionar valor MAIOR que ZERO!")
        else:
            print("Conta não encontrada no banco de dados!")
        return situacao_do_saque
    else:
        conta_no_padrao()[1]

def consultar_saldo(numero_conta: str) -> float | None:
    """Verifica o saldo da conta informada

    Args:
        numero_conta (str): Código da conta que será acessada

    Returns:
        float | None: Retorna o saldo(em float) se a conta existir ou None caso contrário
    """
<<<<<<< HEAD
def consultar_saldo(numero_conta: str) -> float | None:
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()

    if numero_conta in dicionario_do_banco:
        return dicionario_do_banco[numero_conta]["saldo"]
    else:
        return "Nenhuma conta cadastrada"

def somar_saldos_gerais(numero_conta : str) -> float:
    """Soma todos os saldos das contas informadas

    Returns:
        float: Retorna a soma de todas as contas cadastradas
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()

    total = 0.0
    for numero_conta in dicionario_do_banco:
        total += dicionario_do_banco[numero_conta]["saldo"]
    return total
=======
    pass
>>>>>>> 959b0b478707323192bcccf40498769db900dfd2

def somar_saldos_gerais( ) -> float:
    """Soma todos os saldos das contas informadas

<<<<<<< HEAD
def identificar_cliente_mais_rico( ) -> dict | None:
    """Verifica qual cliente possui maior saldo na conta

    Returns:
        dict | None: Retorna todos os dados do cliente com maior saldo. None caso não haja contas no banco
    """
def identificar_cliente_mais_rico() -> dict | None:
        dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
=======
    Returns:
        float: Retorna a soma de todas as contas cadastradas
    """
    pass
>>>>>>> 959b0b478707323192bcccf40498769db900dfd2

def identificar_cliente_mais_rico( ) -> dict | None:
    """Verifica qual cliente possui maior saldo na conta

<<<<<<< HEAD
        maior_saldo = -1
        cliente_mais_rico = None

        for x in dicionario_do_banco.values():
            if x["saldo"] > maior_saldo:
                maior_saldo = x["saldo"]
                cliente_mais_rico = x

        return cliente_mais_rico
=======
    Returns:
        dict | None: Retorna todos os dados do cliente com maior saldo. None caso não haja contas no banco
    """
    pass
>>>>>>> 959b0b478707323192bcccf40498769db900dfd2


def somar_saldos_em_lote(**kwargs) -> int:
    """Soma valores aos saldos de múltiplas contas de uma vez. As chaves dos kwargs serão os números das contas 
    e os valores serão os montantes a serem adicionados.

    Returns:
        int: A quantidade de contas que foram atualizadas com sucesso. Contas inexistentes ou valores negativos 
        serão ignorados.
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    contas_adicionadas = 0
    for conta_no_banco in dicionario_do_banco:
        for conta_a_adicionar in kwargs:
            if conta_no_banco == conta_a_adicionar and kwargs[conta_a_adicionar] > 0:
                contas_adicionadas += 1
                dicionario_do_banco[conta_no_banco]["saldo"] += kwargs[conta_a_adicionar]
                print("alooww")
            else:
                print("deu ruim")
                pass
    return contas_adicionadas
    

        


def subtrair_saldos_em_lote(**kwargs) -> int:
    """Subtrai valores dos saldos de múltiplas contas de uma vez. Falha para uma conta específica se o saldo 
    for insuficiente, mas continua para as outras.

    Returns:
        int: A quantidade de contas que tiveram o saldo removido com sucesso. Contas inexistentes,
        valores negativos ou tentativas de saque maiores que o saldo devem ser ignoradas.
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    contas_adicionadas = 0
    for conta_no_banco in dicionario_do_banco:
        for conta_a_adicionar in kwargs:
            if conta_no_banco == conta_a_adicionar and kwargs[conta_a_adicionar] > 0:
                contas_adicionadas += 1
                dicionario_do_banco[conta_no_banco]["saldo"] -= kwargs[conta_a_adicionar]
            elif (dicionario_do_banco[conta_no_banco]["saldo"] - kwargs[conta_a_adicionar]) < 0:
                pass
            else:
                pass
    return contas_adicionadas

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

if __name__ == "__main__":
    doctest.testmod()