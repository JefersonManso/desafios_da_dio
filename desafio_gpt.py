
"""saldo = 0
depositos = []
saques = []
limite_saque = 500.0
saques_diarios = 3

def depositar(valor):
  global saldo
  if valor > 0:
    saldo += valor
    depositos.append(valor)
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")

  else:
    print("Valor de depósito inválido.")

def sacar(valor):
  global saldo 
  if len(saques) >= saques_diarios:
    print("Limite de saques diários atingido.")
  elif valor > limite_saque:
    print(f"O valor máximo para saque é R${limite_saque:.2f}.")
  elif valor > saldo:
    print("Saldo insuficiente.")
  elif valor > 0:
        saldo -= valor
        saques.append(valor)
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
  else:
        print("Valor de saque inválido.")

def extrato():
    print("\n===== EXTRATO =====")
    print("Depósitos:")
    for deposito in depositos:
        print(f"+ R${deposito:.2f}")

    print("Saques:")
    for saque in extrato.saques:
        print(f"- R${saque:.2f}")


        print(f"Saldo atual: R${saldo:.2f}")
        print("===================\n")

# Exemplo de uso

depositar(1000)
sacar(200)
sacar(300)
sacar(100)  # Excedendo o limite diário
extrato()"""
