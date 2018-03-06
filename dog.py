class Animal:
    tipo = "Mamifero"

    def getTipo(animal):
        return animal.tipo


class Catioro(Animal):
    raca = "vira-lata"


    def __init__(self, nome = "", raca = "", idade = None):
        self.nome = nome
        self.idade = idade
        if raca == '':
            self.raca = "vira lata"
        else:
            self.raca = raca

    def __str__(self):
        return '{} - {} ({})'.format(self.nome, self.raca, self.idade)



doguinho = Catioro("Zeca", idade=3)

print(type(doguinho))
# print(doguinho.nome)
print(doguinho)

# Eh possivel atribuir valor a um atributo ainda nao definido
doguinho.dono = "Maria"
print('O dono eh a {:s}'.format(doguinho.dono))

# Heranca
print("{} eh do tipo {}".format(doguinho, doguinho.getTipo()))