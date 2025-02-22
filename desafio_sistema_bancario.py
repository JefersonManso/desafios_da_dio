
"""CABEÇALHO DO PROGRAMA""" 

print("================================") 
print("    SISTEMA BANCÁRIO v1.0     "  )
print("================================")
# FIM DO CABEÇALHO

# MENU DE OPÇÕES. 
menu = """ 
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

================================
Escolha uma das opções acima: """
# FIM DO MENU DE OPÇÕES.

# VARIÁVEIS GLOBAIS.
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# LAÇO PRINCIPAL (WHILE TRUE) MANTÉM O PROGRAMA RODANDO ATÉ QUE O USUÁRIO ESCOLHA SAIR. 
while True: 

    opcao = input(menu) # EXIBE O MENU E ESPERA O USUÁRIO DIGITAR UMA OPÇÃO.

    if opcao == "1": # OPÇÃO 1: DEPÓSITO
        valor = float(input("Informe o valor do depósito: R$"))

        if valor > 0: # SE VALOR FOR POSITIVO, ELE É ADICIONADO AO SALDO E REGISTRADO NO EXTRATO
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: # SE FOR NEGATIVO OU ZERO, EXIBE UMA MENSAGEM DE ERRO.
            print(" O valor informado é inválido.") 

    elif opcao == "2": # AQUI O USUÁRIO TENTA SACAR DINHEIRO. SE TODAS AS CONDIÇÕES ABAIXO FOREM ATENDIDAS, O SAQUE É FEITO.
        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite diário.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "3": # OPÇÃO 3: EXTRATO, EXIBE TODAS AS TRANSAÇÕES FEITAS.
        print("\n============ EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "4": # OPÇÃO SAIR, SE O USUÁRIO ESCOLHER "4", O PROGRAMA ENCERRA O LOOP E FINALIZA.
     break

    else: # SE O USUÁRIO DIGITAR UMA OPÇÃO QUE NÃO EXISTA NO MENU, É EXIBIDO UM ERRO E PEDE UMA NOVA ENTRADA.
        print("Operação inválida, por favor selecione novamente a operação desejada.")