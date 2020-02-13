#!/usr/bin/python3

# Alinha acima, conhecida como shebang, é opcional e serve para indicar ao linux como executar o script caso seja executado diretamente. O shebang precisa ser a primeira instrucao presente em um arquivo.

# Comentários de uma linha iniciam como #
''' Comentários de
várias linhas
iniciam e terminam com três aspas'''

print('Bonjour le monde')

# print('Qual é o seu nome?')
# nome = input()
# sobrenome = 'Abreu'

a = 5
b = 5.0
c = a / 2
d = b // 2
e = a % 2


print(c)
print(d)
print(e)

msg = 'Minimal Techno Tripping'
size = len(msg)
print('Tamanho de msg:')
print(size)

l = [1, 2, 3]
l2 = []

i = 4
while i >= 0:
	l2.append(i)
	i -= 1

print(l2)

print(type(a))
print(type(b))
print(type(l))



# print('Buenas ' + nome + '! Vlw, flw...')
# print('Buenas', nome, '! Vlw, flw...')

#
# msg = 'Buenas {1} {0}!\n\t Bye bye! numero: {2}'.format(nome, sobrenome, 3)
# print(msg)


# print('hello world')
#
# # Comments in python use a '#'

## WARM UP QUIZ

# PART I
a = 5
b = 5.0
c = a / 2
d = b / 2

# What is type(a)?


# What is type(b)?


# What is c?


# What is d?



# EXERCISES

e = [a, b]
f = list(range(0, 10))

# What is type(e)?


# What is len(e)?


# What is type(f)?


# What are the contents of f?


# What is 'list' called? # hint: google it
