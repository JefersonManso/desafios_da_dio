# MAIÚSCULA, MINÚSCULA E TÍTULO

"""curso = "pYtHon"

print(curso.upper()) #Transforma todas as letras em maiúsculas.

print(curso.lower()) #Transforma todas as letras em minúsculas.

print(curso.title())"""


# ELIMINANDO ESPAÇOS EM BRANCO
"""curso = "    python"
print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())"""

# JUNÇÕES E CENTRALIZAÇÃO
"""curso = "python"

print(curso.center(10, "#"))

print(".".join(curso))"""

# OLD STYLE % (ESTILO ANTIGO NÃO SE USA MAIS EM PYTHON)

"""nome = "Jefeson"
idade = 42
profissao = "Engenheiro"
linguagem = "python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))"""


# MÉTODO FORMAT

"""nome = "Jeferson"
idade = 42
profissao = "Engenheiro"
linguagem = "python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))"""


# MÉTODO F-STRING

"""nome = "Jefrson"
idade= 42
profissao = "Engenheiro"
linguagem = "python"

print(f"Olá, me chamo {nome}, Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")"""


#FORMATAR STRINGS COM F-STRING

"""

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI: 10.2f}")"""


#FATIAMENTO DE STRING

"""nome = "Jeferson Manso Gomes"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])"""

#STRING MÚLTIPLAS LINHAS (TRIPLAS)
#nome = "Jeferson"
#mensagem = f""" 
#Olá, meu nome é {nome},
#Eu estou aprendendo Python"""

#print(mensagem)


#nome = "Jeferson"
#mensagem = f''' 
#   Olá, meu nome é {nome},
#Eu estou aprendendo Python.
#    Essa mensagem tem diferentes recuos.
#'''

#print(mensagem)

#print(""" 
#      ===============MENU===============

#1 - Depositar
#2 - Sacar
#3 - Sair
#      ==================================
#      Obrigado por usar nosso sistema!!!
#      ==================================
#"""
      
#)

