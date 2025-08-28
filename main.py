print("#" * 30)
print("Bem vindo ao Banco Fox!")
print("#" * 30)

resposta = int(input("1 - Operações de Gerente\n2 - Operações de Cliente\n3 - Sair"))
if resposta == 1:

    print("#" * 40)
    print("Modo de Gerente Acessado!\nEscolha uma operação:")
    resposta_gerente = int(input("1 - Verificar saldo total do banco\n" \
    "2 - Identificar cliente mais rico\n" \
    "3 - Adicionar fundos em lotes"))
    
elif resposta == 2:
    pass
else:
    pass