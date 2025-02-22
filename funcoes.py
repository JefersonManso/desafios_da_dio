# FUNÇÕES:

"""def exibir_mensagem():
  print("Olá, Mundo!")

def exibir_mensagem_2(nome="Jeferson", idade = 42, profissao = "Engenheiro"):
  print(f"Seja bem vindo {nome}! Estou vendo que você tem {idade} anos de idade \ne sua profissão é {profissao}.")

def exibir_mensagem_3(nome="Anônimo"):
  print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2()
exibir_mensagem_3()"""

# RETORNANDO VALORES

"""def calcular_total(numeros):
  return sum(numeros)
  

def retorna_antecessor_e_sucessor(numero):
  antecessor = numero -1
  sucessor = numero + 1

  return antecessor, sucessor
calcular_total([10, 20, 34])
retorna_antecessor_e_sucessor(10)

def func_3():
  print("Olá, Mundo!")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())"""

# ARGUMENTOS NOMEADOS

"""def salvar_carro(marca, modelo, ano, placa):
  
  print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # MODELO NÃO MUITO USADO!
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # MELHOR FORMA
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})"""

#POSITIONAL ONLY

"""def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")"""


#KEYWORD ONLY

"""def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")"""


# KEYWORD AND POSITIONAL ONLY

"""def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")"""


# OBJETOS DE PRIMEIRA CLASSE

"""def somar(a, b):
  return a + b

def exibir_resultado(a, b, funcao):
  resultado = funcao(a, b)
  print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)"""

# ESCOPO LOCAL E ESCOPO GLOBAL

"""salario = 2000

def salario_bonus(bonus):
  global salario
  salario += bonus
  return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)"""
