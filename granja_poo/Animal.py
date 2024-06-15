import os
os.system('clear')

class Animal():
    def __init__(self, nombre, animal,salud, hambre, peso):
        self.nombre = nombre
        self.animal = animal
        self.salud  = salud
        self.hambre = hambre
        self.peso   = peso

    def estado(self):
        print(f'{self.animal.capitalize()}')
        print(f'· Nombre: {self.nombre.capitalize()}')
        print(f'· Salud:  {self.salud}')
        print(f'· Hambre: {self.hambre}')
        print(f'· Peso:   {self.peso} kg')

    def comer(self):
        alimento = input('Elije un alimento: manzana +1 kg, elote +2 kg: ')
        return alimento

    def ganar_peso(self):
        alimento = self.comer()
        if alimento == 'manzana':
            self.peso = self.peso + 1
        elif alimento == 'elote':
            self.peso = self.peso + 2

    def edo_salud(self):
        alimento = self.comer()
        if alimento == 'manzana' or alimento == 'elote':
            print(f'{self.nombre} ha comido correctamente')
            self.salud = self.salud + 10
        else:
            print(f'{self.nombre} comió algo incorrecto')
            self.salud = self.salud - 10


    def descansa():
        pass

    def guardados():
        pass

    def pastando():
        pass

    def hacen_popo():
        pass

    def esta_vivo():
        pass


vaca1 = Animal('lola', 'vaca', 100, 'no', 500)
vaca1.estado()
vaca1.ganar_peso()
vaca1.estado()
vaca1.edo_salud()