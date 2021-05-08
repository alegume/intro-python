#!/usr/bin/python3

import sys

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
# LER PEP 257
def define_default_city(state):
    ''' Define a capital do estado de origem como city_origin para um professor existente no arquivo. Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.

    Keyword arguments:
        state -- O estado de origem do professor
    '''
    pass

## Exemplos

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)

# Tamanho
print(len(professor1))
# Chaves
print(professor1.keys())
# Valores
print(professor1.values())

sys.exit(0)

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

# Primeira disciplina
print(professor2['courses'][0])

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
    print(f'{professor1["name"]} Ainda não possui uma cidade')

# 2) Tratar a excecao
try:
    print(professor1['city_origin'])
except KeyError:
    print(f'{professor1["name"]} Ainda não possui uma cidade')


# 3) Usando o metodo get  8-)
# o primeiro parametro eh a chave e o segundo pode ser um valor padrao caso a chave nao exista
# city = professor1.get('city_origin', None)
city = professor1.get('city_origin', 'Canoinhas')
if city == None:
    print(f'{professor1["name"]} Ainda não possui uma cidade')
else:
    print(city)

# Percorrer os elementos pela chaves
for key in professor3.keys():
    value = professor3[key]
    print(key, ':', value)

# Percorrer os elementos pela chaves e valores
for key, value in professor2.items():
    print(key, ':', value)

# Remove chave:valor do dict usando pop(chave)
courses = professor3.pop('courses')
print(professor3)
print(courses)


###
## Exercicios
###


# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente. Ela deve executar sem erro mesmo que alguns dados estejam faltando.
# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro. O algoritmo precisa ser eficiente, nesse caso especifico a melhor a melhor complexidade que pode ser acancada é linear. Algoritmos de complexidade quadratica, cubica, fatorial, etc. não sao considerados como eficientes pois a complexidade linear eh garantida. Como regra geral, se seu algoritmo demorar mais do que alguns segundos, ele, provavelmente, nao eh linear.
