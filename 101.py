# import time, threading

# print('qual é o seu nome?')
# nome = input()
# sobrenome = 'Abreu'
# print('Buenas ' + nome + '! by bye')
#
# msg = 'Buenas {1} {0}!\n\t Bye bye! numero: {2}'.format(nome, sobrenome, 3)
# print(msg)

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
