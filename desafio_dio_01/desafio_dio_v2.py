from datetime import datetime  # Importa o módulo para trabalhar com data e hora

#CABEÇALHO DO PROGRAMA## 

print("================================") 
print("    SISTEMA BANCÁRIO v2.0     "  )
print("================================")
# FIM DO CABEÇALHO

# Inicializa as variáveis do sistema
saldo = 0.0  # Saldo da conta bancária
transacoes = []  # Lista para armazenar as transações (depósitos e saques)
limite_transacoes = 10  # Limite diário de transações

# Função para exibir o menu
def exibir_menu():
    print("\n************* MENU *************")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    print("\n********************************")

# Função para realizar um depósito
def depositar():
    global saldo, transacoes  # Acessa as variáveis globais
    
    if len(transacoes) >= limite_transacoes:
        print("Você atingiu o limite de transações diárias.")
        return
    
    valor = float(input("Digite o valor do depósito: R$ "))  # Solicita o valor do depósito
    if valor > 0:
        saldo += valor  # Atualiza o saldo
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém a data e hora atual
        transacoes.append(("Depósito", valor, data_hora))  # Registra a transação
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O depósito deve ser maior que zero.")

# Função para realizar um saque
def sacar():
    global saldo, transacoes  # Acessa as variáveis globais
    
    if len(transacoes) >= limite_transacoes:
        print("Você atingiu o limite de transações diárias.")
        return
    
    valor = float(input("Digite o valor do saque: R$ "))  # Solicita o valor do saque
    if valor > saldo:
        print("Saldo insuficiente! Não é possível realizar o saque.")  # Verifica se há saldo suficiente
    elif valor > 0:
        saldo -= valor  # Atualiza o saldo
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém a data e hora atual
        transacoes.append(("Saque", -valor, data_hora))  # Registra a transação
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O saque deve ser maior que zero.")

# Função para exibir o extrato
def exibir_extrato():
    print("\n********************************")
    if not transacoes:
        print("Não foram realizadas movimentações.")  # Mensagem caso não haja transações
    else:
        for tipo, valor, data_hora in transacoes:
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")  # Exibe cada transação
    print(f"Saldo atual: R$ {saldo:.2f}")  # Exibe o saldo atual

# Loop principal do sistema
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")  # Solicita a opção do usuário
    
    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break  # Encerra o loop
    else:
        print("Opção inválida! Tente novamente.")
        
