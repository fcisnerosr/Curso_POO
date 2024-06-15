import os; import datetime
os.system('clear')

class Animal():
    def __init__(self, nombre,  genero, animal,salud, hambre, peso):
        self.nombre = nombre
        self.genero = genero
        self.animal = animal
        self.salud  = salud
        self.hambre = hambre
        self.peso   = peso

    def estado(self):
        print(f'{self.animal.capitalize()}')
        print(f'· Nombre: {self.nombre.capitalize()}')
        print(f'· Genero: {self.genero}')
        print(f'· Salud:  {self.salud}')
        print(f'· Hambre: {self.hambre}')
        print(f'· Peso:   {self.peso} kg')

    def comer(self):
        self.alimento = input('Elije un alimento: manzana +1 kg, elote +2 kg: ')
        return self.alimento

    def ganar_peso(self):
        if self.alimento == 'manzana':
            self.peso = self.peso + 1
        elif self.alimento == 'elote':
            self.peso = self.peso + 2

    def edo_salud(self):
        if self.alimento == 'manzana' or self.alimento == 'elote':
            print(f'{self.nombre.capitalize()} ha comido correctamente')
            self.salud = self.salud + 10
        else:
            print(f'{self.nombre.capitalize()} comió algo incorrecto')
            self.salud = self.salud - 10
            print(f'{self.nombre.capitalize()} bajó su salud en 10pts')
            
    def descansa(self):
        now = datetime.datetime.now()
        current_time = now.time()
        if current_time > datetime.time(hour=18, minute=0, second=0) or current_time > datetime.time(hour=4, minute=0, second=0):
            if self.genero == 'hembra':
                print(f'{self.nombre} está despierta, no es hora de dormir')
            else:
                print(f'{self.nombre} está despierto, no es hora de dormir')
        else:
            if self.genero == 'hembra':
                print(f'{self.nombre.capitalize()} está dormida, no la molestes')
            else:
                print(f'{self.nombre.capitalize()} está dormido, no la molestes')

    def guardados():
        pass

    def pastando():
        pass

    def hacen_popo():
        pass

    def esta_vivo():
        pass



vaca1 = Animal('Lola', 'hembra', 'vaca', 100, 'no', 500)
vaca1.estado()
vaca1.descansa()
# vaca1.comer()
# vaca1.ganar_peso()
# vaca1.edo_salud()
# vaca1.estado()

