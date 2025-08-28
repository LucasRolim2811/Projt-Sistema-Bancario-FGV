"""Este módulo deve conter as funções principais relacionadas às operações bancárias. É importante destacar 
que você pode criar funções auxiliares para facilitar a implementação e manter o código organizado. Lembre-se de 
seguir o princípio de responsabilidade única, garantindo que cada função tenha um propósito claro e específico, 
tornando-a mais reutilizável.
O carregamento e salvamento do arquivo CSV devem gerenciados internamente pelas funções, sem a necessidade de 
passar o dicionário de contas como argumento. Para isso, vocês devem usar as funções do módulo banco_de_dados.py 
para ler e salvar o CSV ao realizar as operações."""
import banco_de_dados


def criar_conta(numero_conta: str, nome_cliente: str) -> tuple[int, dict]:
    
    banco_de_dados.salvar_contas_para_csv(contas=(numero_conta, dict("nome_cliente", nome_cliente, "saldo", 0)))
    