#!/usr/bin/python3

## Objetos

class Animal:
	tipo = "Mamifero"

	def getTipo(self):
		return self.tipo


class Catiorro(Animal):
	raca = "vira-lata"

	def __init__(self, nome="", raca="", idade=None):
		self.nome = nome
		self.idade = idade
		if raca == '':
			self.raca = "vira lata"
		else:
			self.raca = raca

	def __str__(self):
		return '{} - {} ({})'.format(self.nome, self.raca, self.idade)

	# # sobrescrita
	# def getTipo(self):
	# 	return "Catiorro"


doguinho = Catiorro("Zeca", idade=3)

print(type(doguinho))
# print(doguinho.nome)
print(doguinho)

# Eh possivel atribuir valor a um atributo ainda nao definido
doguinho.dono = "Maria"
print('O dono eh a {}'.format(doguinho.dono))

# Heranca
print("{1} eh do tipo {0}".format(doguinho.getTipo(), doguinho.nome))






###
# Exercicio
###

