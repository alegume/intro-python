# Funcoes
import sys


def ola(nome='Dilma', idade=0):
	print('ola, ' + nome + '(' + str(idade) + ')')
	print('Ola, {} ({})'.format(nome, idade))
	return 'Acabou'

# ola('alex')
# ola(idade=29, nome='Ale')
# print(sys.version_info)

a = b = c = 0
a1 = 1
b1 = 2
c1 = 3

a1, a = a, a1
l = [x for x in range(100) if x%5==0]

print(l)

# print(a, b, c)
# print(a1, b1, c1)

# print(ola(), '??YASS!!!', sep=' - ')

# x = 1
#
# def funcao():
# 	global x
# 	x += 1
# 	print(x)
#
# funcao()

# x, y = 10, 1
#
# try:
# 	print(x / y)
# except ZeroDivisionError:
# 	print('celoko')

matrix = [
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]
]

print(matrix[1][1])


dict = {'indice1': 'maca', 'fruta2': 'pera'}

for key, value in dict.items():
	print(key, value)
