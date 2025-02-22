#EXEMPLO SEM REPETIÇÃO
# RECEBA UM NÚMERO DO TECLADO E EXIBA OS 2 NÚMEROS SEGUINTES.

"""a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)"""

# EXEMPLO COM REPETIÇÃO
# RECEBA UM NÚMERO DO TECLADO E EXIBA OS 2 NÚMEROS SEGUINTES.

"""a = int(input("Informe um número inteiro: "))
print(a)

repita 2 vezes:
a += 1
print(a)"""

#USO DO FOR

"""texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end=" ")
print()"""

#UTILIZANDO O FOR/ELSE
"""texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end=" ")
else: 
  print()   
  print("Executa no final do laço")"""

#UTILIZANDO RANGE COM FOR
"""for numero in range(0, 11):
  print(numero, end=" ")"""

"""for numero in range(0, 51, 5):
  print(numero,end=" ")"""


#UTILIZANDO O WHILE
"""opcao = -1
while opcao != 0:
  opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

  if opcao == 1:
    print("Sacando...")
  elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")"""

#UTILIZANDO O BREAK
"""while True:
  numero = int(input("Informe um número: "))
  if numero == 10:
    break
  print(numero)"""
