#!/usr/bin/python3

## DICTIONARIES (dicts)

# Os dicts são vetores associativos, tambem conhecidos como maps

# Dicionarios sao semelhantes as listas:
# - ambos podem conter tipos de dados variados
# - ambos sao iteraveis
# - ambos sao mutaveis

# Dicts sao diferentes das listas:
# - dicionarios nao sao ordenados. A ordem nao eh preservada e nao eh importante para essa estrutura de dados
# - o tempo de busca no dicionarioe constante (O(1)), independentemente do tamanho do dicionario

# Dicts são como dicionarios reais:
# - os dicts são feitos de pares 'chave':valor
# - as chaves do dicts devem ser unicas
# - a chave serve para procurar o valor, mas não o contrário

# Apenas uma funcao vazia. Voce ira implementa-la futuramente :p
def define_default_city(state):
	''' Desc: Esta funcao define uma cidade padrao para um professor. A cidade padrao eh a capital do estado de origem.
		In: (dict) um professor
		Out: (bool) True se a capital do estado de origem puder ser definida e False caso contrario
	'''
	pass

## Exemplos

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

# Utilizando construtor
professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
print(professor3)

# adicionando chave e valor em um dict jah existente
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
print(professor3)

# Acessar um valor em um dict
print(professor1['state_origin'])

# Tentar acessar um valor em um dict usando uma chave inexistente
# KeyError exception
# print(professor1['city_origin'])

## Tres formas de contornar o erro

# 1) Simples e direta
if 'city_origin' in professor1:
	print(professor1['city_origin'])
else:
	print('{} Ainda não possui uma cidade'.format(professor1['name']))

# 2) Tratar a excecao
try:
	print(professor1['city_origin'])
except KeyError:
	print('{} Ainda não possui uma cidade'.format(professor1['name']))


# 3) Usando o metodo get  8-)
# o primeiro parametro eh a chave e o segundo pode ser um valor padrao caso a chave nao exista
# city = professor1.get('city_origin', None)
city = professor1.get('city_origin', 'Canoinhas')
if city == None:
	print('{} Ainda não possui uma cidade'.format(professor1['name']))
else:
	print(city)
