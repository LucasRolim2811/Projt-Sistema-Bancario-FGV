import banco_de_dados
import doctest
#########################################################################################

def conta_no_padrao(numero_conta:str) -> tuple[bool, str]:
    """Verifica se o numero da conta é menor que 9999 e se possui 4 caracteres

    Args:
        numero_conta (str): String correspondente ao numero da conta que deve ser analisado

    Returns:
        tuple[bool, str]: Tupla respondendo se o número da conta satisfaz as condições(bool) e com uma mensagem de feedback(str)

    Exemplos:
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

    Exemplos:
    >>> criar_conta("0000", "EMAP")
    ('0000', {'nome_cliente': 'EMAP', 'saldo': 0.0})
    >>> criar_conta("0001", "EBAPE")
    ('0001', {'nome_cliente': 'EBAPE', 'saldo': 0.0})
    >>> criar_conta("0000", "EMAP") #Com a conta "EMAP" já criada acima
    Esta conta já existe! Por favor, senhor gerente, colocar uma conta ainda não criada!
    >>> criar_conta("00000", "EMAP")
    Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    if conta_no_padrao(numero_conta)[0]:
        if numero_conta not in dicionario_do_banco:
            dicionario_do_banco[numero_conta] = {"nome_cliente": nome_cliente,"saldo": 0}
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            conta_criada = banco_de_dados.carregar_contas_de_csv()[numero_conta]
            return (numero_conta, conta_criada)
        else:
            print("Esta conta já existe! Por favor, senhor gerente, colocar uma conta ainda não criada!")
    else:
        print(conta_no_padrao(numero_conta)[1])
        
    

def depositar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Deposita um valor dado no saldo da conta especificada

    Args:
        numero_conta (str): Código da conta que se deseja fazer o depósito
        valor (float): Valor que se deseja depositar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    
    Exemplos:
    >>> depositar("0000", 1000)
    (True, 'Depósito realizado com sucesso!')
    >>> depositar("0000", -1000)
    (False, 'Adicionar um valor MAIOR QUE ZERO!')
    >>> depositar("0004", 1000)
    (False, 'Conta inexistente!')
    >>> depositar("00000", 1000)
    Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    situacao_do_deposito = tuple()
    if conta_no_padrao(numero_conta)[0]:
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
        print(conta_no_padrao(numero_conta)[1])


def sacar(numero_conta: str, valor: float) -> tuple[bool, str]:
    """ Faz um saque na conta especificada. Subtrai o valor diretamente do saldo da conta

    Args:
        numero_conta (str): Código da conta que se deseja fazer o saque
        valor (float): Valor que se deseja sacar

    Returns:
        tuple[bool, str]: Retorna se foi possível fazer o depósito[True/False] e uma mensagem de feedback
    
    Exemplos:
    >>> sacar("0000", 500)
    (True, 'Valor sacado com sucesso')
    >>> sacar("0000", -10000.0)
    (False, 'Adicionar valor MAIOR QUE ZERO!')
    >>> sacar("9999", 10000.0)
    (False, 'Conta não encontrada no banco de dados!')
    >>> sacar("Eu amo a EMAP", 10000.0)
    Nossas contas tem o padrão de 0001, 0002,..., 9999. Por favor, respeite o limite de contas ou coloque um número válido
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    situacao_do_saque = ()
    if conta_no_padrao(numero_conta)[0]:
        if numero_conta in dicionario_do_banco:
            saldo_positivo = dicionario_do_banco[numero_conta]["saldo"] - valor > 0
            if saldo_positivo and valor > 0:
                dicionario_do_banco[numero_conta]["saldo"] -= valor
                banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
                situacao_do_saque = (True, "Valor sacado com sucesso")
            elif valor < 0:
                situacao_do_saque = (False, "Adicionar valor MAIOR QUE ZERO!")
        else:
            situacao_do_saque = (False, "Conta não encontrada no banco de dados!")
        return situacao_do_saque
    else:
        print(conta_no_padrao(numero_conta)[1])


def consultar_saldo(numero_conta: str) -> float | None:
    
    """Verifica o saldo da conta informada

    Args:
        numero_conta (str): Código da conta que será acessada

    Returns:
        float | None: Retorna o saldo(em float) se a conta existir ou None caso contrário
    
    Exemplos:
    >>> consultar_saldo("9999")
    'Esta conta ainda não foi cadastrada!'
    
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    saldo = None
    if numero_conta in dicionario_do_banco:
        saldo = dicionario_do_banco[numero_conta]["saldo"]
        return saldo
    else:
        return "Esta conta ainda não foi cadastrada!"

def somar_saldos_gerais() -> float:
    """Soma todos os saldos das contas informadas

    Returns:
        float: Retorna a soma de todas as contas cadastradas
    
    Exemplos:
    >>> somar_saldos_gerais()
    500.0
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    total = 0.0
    for numero_conta in dicionario_do_banco:
        total += dicionario_do_banco[numero_conta]["saldo"]
    return total

def identificar_cliente_mais_rico() -> dict | None:
    """Identifica qual cliente possui maior saldo bancário.

    Returns:
        dict | None: Retorna o dicionário da conta do cliente com maior saldo ou None caso não haja ninguém no banco de dados
    
    Exemplos:
    >>> identificar_cliente_mais_rico()
    {'nome_cliente': 'EMAP', 'saldo': 1000.0}
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    saldo_mais_rico = 0
    cliente_mais_rico = ""

    for conta in dicionario_do_banco:
            if dicionario_do_banco[conta]["saldo"] > saldo_mais_rico:
                saldo_mais_rico = dicionario_do_banco[conta]["saldo"]
                cliente_mais_rico = conta
    if saldo_mais_rico == 0:
        return None

    return dicionario_do_banco[cliente_mais_rico]


def somar_saldos_em_lote(**kwargs) -> int:
    """Soma valores aos saldos de múltiplas contas de uma vez. As chaves dos kwargs serão os números das contas 
    e os valores serão os montantes a serem adicionados"""

    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    contas_adicionadas = 0
    for numero_conta, valor_a_adicionar in  kwargs.items():
        if numero_conta in dicionario_do_banco and valor_a_adicionar > 0:
            dicionario_do_banco[numero_conta]["saldo"] += valor_a_adicionar
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            contas_adicionadas += 1
    
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
    for numero_conta, valor_a_adicionar in  kwargs.items():
        if numero_conta in dicionario_do_banco and valor_a_adicionar > 0:
            dicionario_do_banco[numero_conta]["saldo"] -= valor_a_adicionar
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            contas_adicionadas += 1
    
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

    Examplos:
    >>> realizar_transferencia("0000", "0001", 250)
    (True, 'Transferência realizada com sucesso!')
    >>> realizar_transferencia("0000", "9999", 3000)
    (False, 'Uma conta não existe no banco de dados')
    >>> realizar_transferencia("0000", "0001", 10000000)
    (False, 'Saldo da conta é insuficiente')
    """
    dicionario_do_banco = banco_de_dados.carregar_contas_de_csv()
    if conta_origem and conta_destino in dicionario_do_banco:
        saldo_origem = dicionario_do_banco[conta_origem]["saldo"]
        if saldo_origem - valor > 0:
            dicionario_do_banco[conta_origem]["saldo"] -= valor
            dicionario_do_banco[conta_destino]["saldo"] += valor
            banco_de_dados.salvar_contas_para_csv(contas=dicionario_do_banco)
            return (True, "Transferência realizada com sucesso!")
        else:
            return (False, "Saldo da conta é insuficiente")
    else:
        return (False, "Uma conta não existe no banco de dados") 

if __name__ == "__main__":
    doctest.testmod(verbose=True)