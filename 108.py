#!/usr/bin/python3

from datetime import date

## Classes e Objetos

# Primeira classe
class Animal:
	# atributo comum
	tipo = "Mamifero"

	# metodo da classe
	def get_tipo(self):
		return self.tipo


# Segunda classe
class Catiorro(Animal):
	# Atributo protegido (protected)
	_data_criacao_ = date.today()

	# dunder init dunder eh o construtor da classe. Dunder = double underscore
	# self eh uma referencia ao objeto. Pode ser usado outro nome, mas nao eh comum.
	def __init__(self, nome='', raca='', idade=None):
		self.nome = nome
		self.idade = idade
		if raca == '':
			self.raca = "vira lata"
		else:
			self.raca = raca

	# outro metodo privado e 'magico'
	# metodos magicos: https://www.python-course.eu/python3_magic_methods.php
	def __str__(self):
		return '{} - {} ({})'.format(self.nome, self.raca, self.idade)

	def imprimir_criacao(self):
		# formatacao da data com strftime
		print(self._data_criacao_.strftime('%d/%m/%Y'))

	# # sobrescrita
	# def get_tipo(self):
	# 	return "Catiorro"


## Utilizacao das classes

# Instancializacao de objeto
doguinho = Catiorro("Zeca", idade=3)

print(type(doguinho))
# print(doguinho.nome)
print(doguinho)

# Eh possivel atribuir valor a um atributo ainda nao definido
doguinho.dono = "Maria"
print('O dono eh a {}'.format(doguinho.dono))

# Heranca
print("{1} eh do tipo {0}".format(doguinho.get_tipo(), doguinho.nome))

# Instancializacao de outro objeto
dog1 = Catiorro()
doguinho.imprimir_criacao()
