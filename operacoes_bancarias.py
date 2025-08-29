"""Este módulo deve conter as funções principais relacionadas às operações bancárias. É importante destacar 
que você pode criar funções auxiliares para facilitar a implementação e manter o código organizado. Lembre-se de 
seguir o princípio de responsabilidade única, garantindo que cada função tenha um propósito claro e específico, 
tornando-a mais reutilizável.
O carregamento e salvamento do arquivo CSV devem gerenciados internamente pelas funções, sem a necessidade de 
passar o dicionário de contas como argumento. Para isso, vocês devem usar as funções do módulo banco_de_dados.py 
para ler e salvar o CSV ao realizar as operações."""
import banco_de_dados
#########################################################################################

"""
CRIAR CONTA
Descrição: Deve criar uma conta nova, incluindo no csv. 
Note que essa conta deve começar com um saldo de 0 reais.

Retorno: Uma tupla com o numero da nova conta criada e 
o dicionário completo dela (ex: (0001, {"cliente": "Joao", "saldo": 0.00}))."""

def criar_conta(numero_conta: str, nome_cliente: str) -> tuple[int, dict]:
    banco_de_dados.salvar_contas_para_csv(contas=(numero_conta, dict("nome_cliente", nome_cliente, "saldo", 0)))


########################################################################################

"""
SOMAR SALDOS GERAIS
Descrição: Soma o saldo de todas as contas existentes no banco.

Retorno: O valor total (float) da soma de todos os saldos."""

def somar_saldos_gerais( ) -> float:
    pass


#########################################################################################
"""
DEPOSITAR
Descrição: Se a conta existir e o valor for positivo, adiciona o valor ao saldo.

Retorno: Uma tupla indicando sucesso/falha com uma mensagem apropriada (ex: (False, "Erro: conta inexistente."))."""

def depositar(numero_conta: str, valor: float) -> tuple[bool, str]:
    pass


#########################################################################################

"""
SACAR
Descrição: Verifica se a conta existe, se o valor é positivo e se há saldo suficiente. Se tudo estiver OK, subtrai o valor do saldo.

Retorno: Uma tupla indicando sucesso/falha com uma mensagem apropriada (ex: (False, "Erro: saldo insuficiente."))."""

def sacar(numero_conta: str, valor: float) -> tuple[bool, str]:
    pass


###########################################################################################

"""
CONSULTAR SALDO
Descrição: Procura pela conta no dicionário e retorna o saldo dela.

Retorno: O saldo (um float) se a conta existir, ou None se não existir."""

def consultar_saldo(numero_conta: str) -> float | None:
    pass


############################################################################################

"""
IDENTIFICAR CLIENTE MAIS RICO
Descrição: Percorre todas as contas e identifica qual cliente possui o maior saldo.

Retorno: O dicionário completo da conta com o maior saldo (ex: {"cliente": "Carlos", "saldo": 5000.00}). 
Se não houver contas, retorna None."""

def identificar_cliente_mais_rico() -> dict | None:
    pass


#############################################################################################

"""
SOMAR SALDOS EM LOTE
Descrição: Soma valores aos saldos de múltiplas contas de uma vez. As chaves dos kwargs serão os 
números das contas e os valores serão os montantes a serem adicionados.

Retorno: A quantidade de contas que foram atualizadas com sucesso. 
Contas inexistentes ou valores negativos devem ser ignorados."""


def somar_saldos_em_lote(**kwargs) -> int:
    pass

##############################################################################################

"""
SUBTRAIR SALDOS EM LOTE
Descrição: Subtrai valores dos saldos de múltiplas contas de uma vez. Falha para uma conta específica 
se o saldo for insuficiente, mas continua para as outras.

Retorno: A quantidade de contas que tiveram o saldo removido com sucesso. Contas inexistentes, 
valores negativos ou tentativas de saque maiores que o saldo devem ser ignoradas."""

def subtrair_saldos_em_lote(**kwargs) -> int:
    pass

#################################################################################################

def realizar_transferencia():
    pass

