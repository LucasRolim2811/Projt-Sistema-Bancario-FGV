from time import sleep

print("#" * 30)
print("Bem vindo ao Banco Fox!")
print("#" * 30)

resposta = 0

while not resposta == 3:
	resposta = int(input("1 - Operações de Gerente\n2 - Operações de Cliente\n3 - Sair"))
	if resposta == 1:
		print("#" * 40)
		print("Modo de Gerente Acessado!\nEscolha uma operação:")
		resposta_gerente = int(input("1 - Verificar saldo total do banco\n" \
								"2 - Identificar cliente mais rico\n" \
							"3 - Adicionar fundos em lotes\n" \
						"4 - Debitar fundos em lote\n" \
					"5 - Abrir uma nova conta no banco\n" \
				"6 - Voltar ao menu principal "))
		
	
	
	elif resposta == 2:
		print("#" * 40)
		
		
		print("Modo de Cliente acessado!!\nEscolha uma operação:")
		resposta_cliente = int(input("1 - Consultar meu saldo\n" \
							   "2 - Realizar um depósito\n" \
						"3 - Realizar um saque\n" \
					"4 - Realizar uma transferênci\n"
				"5 - Voltar ao menu principal"))
		

	elif resposta == 3:
		print("Encerrando")
		print("...")
		sleep(1.5)
		print("Obrigado e até a próxima")

"""
funções:
criar_conta
depositar
sacar
consultar_saldo
somar_saldos_gerais
identificar_cliente_mais_rico
somar_saldos_em_lote
subtrair_saldos_em_lote
realizar_transferencia

f



"""