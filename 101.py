#!/usr/bin/python3

# Alinha acima, conhecida como shebang, é opcional e serve para indicar ao linux como executar o script caso seja executado diretamente. O shebang precisa ser a primeira instrucao presente em um arquivo.

# Comentários de uma linha iniciam como #

''' Comentários de
várias linhas
iniciam e terminam com três aspas'''

print('Bonjour le monde')

a = 5
b = 5.0
c = a / 2
d = b // 2
e = a % 2

print(c)
print(d)
print(e)

# Tipo de um objeto (tudo eh objeto em python)
print(type(a))
print(type(b))

# Metodos disponiveis para o objeto
print(dir(a))
print(dir(b))

# Ajuda para o objeto
print(help(a))
print(help(b))
