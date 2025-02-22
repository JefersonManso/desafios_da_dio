#USO DO (IF)
"""saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
  print("Realizando saque...")
if saldo < saque:
  print("Saldo insuficiente!")"""

#USO DO (IF/ELSE)
"""saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
  print("Realizando saque...")
else:
  print("Desculpe, Saldo insuficiente!")"""


# USO DO If/elif/else
"""opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
  valor = float(input("Informe a quantia para o saque: "))
  #...
elif opcao == 2:
  print("Exibindo o extrato...")
else:
  sys.exit("Opção inválida")"""


#IF ANINHADO
"""if conta_normal:	
  if saldo >= saque:		
    print("Saque realizado com sucesso!")	
  elif saque <= (saldo + cheque_especial):		
    print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:	
  if saldo >= saque:		
    print("Saque realizado com sucesso!")	
  else:		
    print("Saldo insuficiente!")"""

#IF TERNÁRIO
"""status = "Sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque!")"""

#EXEMPLO
"""MAIOR_IDADE = 18
idade = int(input("Informe a sua idade: "))
if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar a CNH!")

else: 
  print("Ainda não pode tirar a CNH!")"""


#ESTRUTURA_CONDICIONAL_ANINHADA

"""conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

  if saldo >= saque:
    print("Saque realizado com sucesso!")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial!")
  else:
    print("Não foi possível realizar o saque!")
  
elif conta_universitaria:

  if saldo >= saque:
    print("Saque realizado com sucesso!")
  else:
    print("Saldo insuficiente!")

elif conta_especial:

  print("Conta especial selecionada!")
else:
  print("o sistema não reconheceu o seu tipo de conta, entre em contato com o seu gerente.")"""


#ESTRUTURA CONDICIONAL TERNÁRIA

"""saldo = 2000
saque = 3000

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")"""