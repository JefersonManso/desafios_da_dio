# # Importações
from datetime import datetime
from abc import ABC, abstractmethod

# CABEÇALHO DO PROGRAMA 

print("================================") 
print("    SISTEMA BANCÁRIO v2.0     "  )
print("================================")
# FIM DO CABEÇALHO

class Cliente:
    """Classe que representa um cliente do banco."""
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
    
    def adicionar_conta(self, conta): # Adiciona uma conta ao cliente.         
        self.contas.append(conta)

class Conta: # Classe base para contas bancárias.
    def __init__(self, numero, cliente):
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()
    
    def depositar(self, valor): # Realiza um depósito na conta.
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao("Depósito", valor)
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n Operação falhou! Valor inválido.")
    
    def sacar(self, valor): # Realiza um saque na conta.
        if valor <= 0:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
        
        if valor > self.saldo:
            print("\nOperação falhou! Saldo insuficiente.")
            return False
        
        self.saldo -= valor
        self.historico.adicionar_transacao("Saque", valor)
        print("\n=== Saque realizado com sucesso! ===")
        return True
    
    def exibir_extrato(self): # Exibe o extrato da conta.
        print("\n=== Extrato ===")
        for transacao in self.historico.transacoes:
            print(f"{transacao['data_hora']}: {transacao['tipo']} - R$ {transacao['valor']:.2f}")
        print(f"\nSaldo: R$ {self.saldo:.2f}")

class Historico:
    # Classe que representa o histórico de transações de uma conta.
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, tipo, valor):
        #Adiciona uma transação ao histórico.
        if len(self.transacoes) < 10:  # Limite de 10 transações
            self.transacoes.append({
                "tipo": tipo,
                "valor": valor,
                "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            })
        else:
            print("\nHistórico de transações cheio!")

# Funções auxiliares
def criar_cliente(contas):
    # Cria um novo cliente e adiciona à lista de contas.
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cliente = Cliente(nome, cpf, endereco)
    conta = Conta(numero=len(contas) + 1, cliente=cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("\n=== Cliente e conta criados com sucesso! ===")

def listar_contas(contas):
    #Lista todas as contas e seus respectivos clientes.
    if not contas:
        print("\nNão há contas cadastradas.")
        return
    
    print("\n=== Lista de Contas ===")
    for conta in contas:
        print(f"Conta: {conta.numero} | Cliente: {conta.cliente.nome} | CPF: {conta.cliente.cpf}")

def main():
    contas = []
    
    while True: # Loop do menu
        print("\n=== Menu ===")
        print("1. Nova conta")
        print("2. Listar contas")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")
        
        opcao = input("Digite a opção desejada: ") # Solicita ao usuário a opção desejada
        # Lógica para tratar cada uma das opções.
        if opcao == "1":
            criar_cliente(contas) # Cria um novo cliente e conta
        elif opcao == "2":
            listar_contas(contas) # Lista todas as contas.
        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: ")) # Solicita o número da conta para depósito.
            for conta in contas: # Procura a conta pelo número.
                if conta.numero == numero_conta:
                    valor = float(input("Digite o valor do depósito: R$ ")) # Solicita o valor do depósito.
                    conta.depositar(valor) # Realiza o depósito na conta.
                    break
            else:
                print("\nConta não encontrada.")  # Caso a conta não seja encontrada.
        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            for conta in contas: # Procura a conta pelo número.
                if conta.numero == numero_conta:
                    valor = float(input("Digite o valor do saque:R$ ")) # Solicita o valor do saque.
                    conta.sacar(valor) # Realiza o saque na conta.
                    break
            else:
                print("\nConta não encontrada.") # Caso a conta não seja encontrada.
        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: ")) # Solicita o número da conta para exibir o extrato.
            for conta in contas: # Procura a conta pelo número.
                if conta.numero == numero_conta:
                    conta.exibir_extrato() # Exibe o extrato da conta.
                    break
            else:
                print("\nConta não encontrada.")  # Caso a conta não seja encontrada.
        elif opcao == "6":
            print("\n=== Saindo do sistema... ===") # Finaliza o sistema.
            break
        else:
            print("\nOpção inválida.") # Caso a opção digitada não seja válida.
            
# Verifica se o script está sendo executado diretamente e, se sim, chama a função main
if __name__ == "__main__":
    main()
