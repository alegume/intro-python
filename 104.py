#!/usr/bin/python3

'''
	DESAFIO!!!
	1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
	2) Agora faca sem utilizar uma terceira variavel temporaria.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## Functions

# Define a funcao
def sum(x=3, y=5):
	print("x: " + str(x))
	print("y: " + str(y))
	return x + y

# Chamada simples de funcao
x = 1
y = 2
z = sum(x, y)
print(z)

# Chamada de funcao com parametro sem ordem
z = sum(y=10, x=13)
print(z)

# Utiliza valor padrao dos parametros
z = sum()
print(z)

# Atribuicao para mais de uma variável
a, b = x, y
print('a: {}; b:{}'.format(a, b))

list = [1, 2, 3]
a, b, c = list
print('a: {}; b:{}; c:{}'.format(a, b, c))

# troca de valores
a, b = b, a
print('a: {}; b:{}'.format(a, b))

## Conditionals

temperature = 4
if temperature <= 0:
	print('Solido')
elif temperature > 0 and temperature < 100:
	print('Liquido')
else:
	print('Gasoso')

# Notacao matematica
if 0 < temperature < 100:
	print('Liquido')

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
# OBS.: Utilize apenas o que foi estudado ate agora
