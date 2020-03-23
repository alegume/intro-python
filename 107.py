#!/usr/bin/python3

import sys
import timeit

## Tuplas x listas

#  As tuplas sao estruturas 'menores' e mais rapidas que as listas para se armazenar dados de maneira ordenada. Ao contrario das listas, as tuplas sao imutaveis (immutable).
# Ou seja, uma vez que sao criadas, as tuplas sao estaticas e isso garante uma melhor performance nos casos em que podem ser aplicadas.
# As listas demandam um maior custo, mas permitem adicionar, remover e alterar os seus dados. Ou seja, a lista é mutavel.

# lista
list = [2, 3, 5, 7, 11, 13, 17, 19]
# tupla
tuple = (2, 3, 5, 7, 11, 13, 17, 19)

# Mesmo tamanho
print(len(list))
print(len(tuple))

# iteracao identica
for p in list:
	print(p)
for p in tuple:
	print(p)

# tamanho das tuplas eh bem menor. Pode ser significante ao se trabalhar com grande quantidade de dados
print('Tamanho lista: ', sys.getsizeof(list))
print('Tamanho tupla: ', sys.getsizeof(tuple))
# tamanho de um range (lembram da ultima aula?)
print('Tamanho range: ', sys.getsizeof(range(9)))
print('Tamanho range: ', sys.getsizeof(range(999999999999999999)))

# por ser imutavel, as tuplas sao criadas mais rapidamente
# tempo para cria um milhao de listas e tuplas (aumente essa quantidade, progressivamente, para perceber o efeito)
list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print('Tempo lista:', list_time)
print('Tempo tupla:', tuple_time)

print('{}% mais rapido'.format(tuple_time / list_time * 100))


# as tuplas nao precisam dos parenteses para serem criadas

t1 = (1, 2)
t2 = 1, 2
survey = (22, "Timor Leste", False)

print(type(t1))
print(type(t2))
print(t1 == t2)

# unpack de tupla ;P
age, country, knows_python = survey
print('idade: {}; país: {}; sabe python: {}'.format(age, country, knows_python))

# Acesso por indice
print(survey[1])






###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py