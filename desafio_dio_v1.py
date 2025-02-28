
CABEÇALHO DO PROGRAMA 

print("================================") 
print("    SISTEMA BANCÁRIO v1.0     "  )
print("================================")
# FIM DO CABEÇALHO

# Inicializa o saldo sa conta
saldo = 0
depositos = [] # Lista para armazenar os depósitos
saques = [] # Lista para armazenar os saques
limite_saque = 500.0 # Limite de saque por operação
saques_diarios = 3 # Número máximo de saques por dia
saques_realizados = 0 # Contador para registrar a quantidade de saques realizados por dia.

# Loop principal do menu
while True:
    # Exibe o menu de opções para o usuário
    print("\n*********** MENU ***************\n")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair\n")
    print("********************************")
    opcao = input("Escolha uma das opções acima: ") # Usuário escolhe uma opção

    # Opção de depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito:R$ ")) # Usuário informa o valor de depósito
        if valor > 0: # Verifica se o valor é positivo
            saldo += valor # Adiciona o valor ao saldo
            depositos.append(valor) # Armazena o depósito na lista
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    # Opção de saque
    elif opcao == "2":
        if saques_realizados >= saques_diarios: # Verifica se o usuário fez os 3 saques ao dia
            print("Limite de saques diários atingido.")
        else:
            valor = float(input("Informe o valor do saque:R$ ")) # Solicita o valor do saque
            if valor > limite_saque: # Verifica se o saque não ultrapassa o limite permitido
                print(f"O valor máximo para saque é R${limite_saque:.2f}.")
            elif valor > saldo: # Verifica se há saldo suficiente
                print("Saldo insuficiente.")
            elif valor > 0:
                saldo -= valor # Subtrai valor do saldo
                saques.append(valor) # Armazena o saque na lista
                saques_realizados += 1 # Incrementa o contador de saques do dia
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor de saque inválido.")

    # Opção de extrato
    elif opcao == "3":
        print("\n=========== EXTRATO ===========")
        print("Depósitos:")
        for deposito in depositos: # Percorre a lista de depósitos e exibe cada um
            print(f"+ R${deposito:.2f}")
        print("Saques:")
        for saque in saques: # Percorre a lista de saques e exibe cada um
            print(f"- R${saque:.2f}")
        print(f"Saldo atual: R${saldo:.2f}") # Exibe o saldo atual da conta
        print("===============================\n")

    # Opção para sair do sistema
    elif opcao == "4":
        print("Saindo do sistema...")
        break # Encerra o loop e finaliza o programa
    
    # Caso o usuário escolha uma opção inválida
    else:
        print("Opção inválida. Tente novamente.")
