#!/usr/bin/python3

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















# def msg():
# 	time.sleep(17)
# 	print("Acordei")
#

# try:
# 	print("dormi")
# 	Tobj = threading.Thread(target=msg)
# 	Tobj.start()
#
# 	inicio = time.time()
# 	a = 1
# 	for i in range(3):
# 		a = i*i
# 		time.sleep(1)
# 		print(i)
#
# 	fim = time.time()
# 	print(fim - inicio)
#
# 	print("acaboooou")
#
# except KeyboardInterrupt:
# 	print('\n\tTchau kerida!')

# x = int(input())
#
# if x < 0:
# 	msg = "Negativo"
# elif x > 0:
# 	msg = "Positivo"
# else:
# 	msg = "Zer0"
#
# print(msg)














import random, time
try:
	while True:
		par = impar = 0
		for i in range(4):
			n = random.randint(1, 2)

			if n % 2:
				par += 1
				print(n)
			else:
				impar += 1
				time.sleep(1)

			print(n)

		print("par: {}    |     impar: {}".format(par, impar))
except KeyboardInterrupt:
	print('\n\tthcau kerida')
