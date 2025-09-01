from time import sleep
import banco_de_dados
import operacoes_bancarias
resposta = 0

while not resposta == 3:
	print("#" * 30)
	print("Bem vindo ao Banco Fox!")
	print("#" * 30)
	
	resposta = int(input("1 - Operações de Gerente\n2 - Operações de Cliente\n3 - Sair"))
	
	
	
	print("=" * 50)
	caminho_arquivo: str = "contas.csv"
	numero_conta = int(input("  Sistema Seguro - Acesso Restrito  \n  Login necessário para continuar:"))
	contas = banco_de_dados.carregar_contas_de_csv(numero_conta,caminho_arquivo)
	

	if numero_conta in contas:
    		
		print("Login válido")
		
		#PARTE GERENTE
		if resposta == 1:
			
			print("#" * 40)
			print("Modo de Gerente Acessado!\nEscolha uma operação:")
			resposta_gerente = int(input("1 - Verificar saldo total do banco\n" \
									"2 - Identificar cliente mais rico\n" \
								"3 - Adicionar fundos em lotes\n" \
							"4 - Debitar fundos em lote\n" \
						"5 - Abrir uma nova conta no banco\n" \
					"6 - Voltar ao menu principal "))
			if resposta_gerente == 1:
				operacoes_bancarias.somar_saldos_gerais()
			
			elif resposta_gerente == 2:
				operacoes_bancarias.identificar_cliente_mais_rico()
			
			elif resposta_gerente == 3:
				kwargs = 0
				operacoes_bancarias.somar_saldos_em_lote(**kwargs)
			
			elif resposta_gerente == 4:
				operacoes_bancarias.subtrair_saldos_em_lote(**kwargs)
			
			elif resposta_gerente == 5:
				nome_cliente = str("Digite seu nome:")
				operacoes_bancarias.criar_conta(numero_conta, nome_cliente)
				
			elif resposta_gerente == 6:
				pass

		
		#PARTE CLIENTE
		elif resposta == 2:
			print("#" * 40)	
			print("Modo de Cliente acessado!!\nEscolha uma operação:")
			resposta_cliente = int(input("1 - Consultar meu saldo\n" \
								"2 - Realizar um depósito\n" \
							"3 - Realizar um saque\n" \
						"4 - Realizar uma transferênci\n"
					"5 - Voltar ao menu principal"))
			if resposta_cliente == 1:
				print("#" * 40)
				print(f" ----- Setor de Consulta de Saldo Acessado! ----- ")
				sleep(0.5)
				numero_conta = str(input("Digite o número de sua conta: "))
				print("-"* 7)
				print(f"Acessando dados da conta [{numero_conta}] ...")
				sleep(1)
				operacoes_bancarias.consultar_saldo(numero_conta)

			elif resposta_cliente == 2:
				
				print("#" * 40)
				print(" ----- Setor de Deposito Acessado!! ----- ")
				numero_conta = str(input("Digite o número de sua conta: "))
				print("-"* 10)
				valor = float("Digite o valor que deseja depositar:")
				operacoes_bancarias.depositar(numero_conta, valor)
			
			elif resposta_cliente == 3:
				print("#" * 40)
				print(" ----- Setor de Saque Acessado!! -----  ")
				numero_conta = str(input("Digite o número de sua conta\n: "))
				print("-"* 10)
				valor = float(input("Digite o valor que deseja sacar:"))
				operacoes_bancarias.sacar(numero_conta, valor)
				
				
			elif resposta_cliente == 4:
				print(" ----- Setor de Transferência Acessado!! ----- ")
				conta_origem = str(input("Digite novamente o número de sua conta: "))
				print("-"*10)
				conta_destino = str(input("Digite o número da conta de destino\n:"))
				operacoes_bancarias.realizar_transferencia(conta_origem, conta_destino, valor)

			elif resposta_cliente == 5:
				pass												

	elif resposta == 3:
		print("Encerrando")
		print("...")
		sleep(1.5)
		print("Obrigado e até a próxima!!!")
		break
	else:
    		
		print("Login inválido")
		pass

"""
funções:
criar_conta()
depositar()
sacar()
consultar_saldo()
somar_saldos_gerais()
identificar_cliente_mais_rico()
somar_saldos_em_lote()
subtrair_saldos_em_lote()
realizar_transferencia()





"""