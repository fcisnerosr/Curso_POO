import os; import datetime
os.system('clear')

class Animal():
    def __init__(self, nombre,  genero, animal,salud, peso, ubicacion):
        self.nombre     = nombre
        self.genero     = genero
        self.animal     = animal
        self.salud      = salud        
        self.peso       = peso
        self.ubicacion  = ubicacion

    now = datetime.datetime.now()
    current_time = now.time()
    print(now)

    def estado(self):
        print(f'{self.animal.capitalize()}')
        print(f'· Nombre:       {self.nombre.capitalize()}')
        print(f'· Genero:       {self.genero}')
        print(f'· Salud:        {self.salud}')
        print(f'· Hambre:       {self.hambre}')
        print(f'· Peso:         {self.peso} kg')
        print(f'· Ubicación:    {self.ubicacion}')

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

    def guardate(self):
        if self.ubicacion == 'cabaña':
            print(f'{self.animal} guardada')
        elif self.ubicacion == 'área verde':
            print(f'{self.animal} voy para allá')
            self.ubicacion = 'cabaña'
        else:
            print(f'{self.animal} está perdida')

    def ponte_a_pastar(self):
        pass
        # if self.hambre == 'si':
        #     print(f'')

    def hacen_popo():
        pass

    def esta_vivo():
        pass



vaca1 = Animal('Lola', 'hembra', 'vaca', 100, 500, 'área verde')
vaca1.estado()
vaca1.descansa()
vaca1.guardate()
# vaca1.comer()
# vaca1.ganar_peso()
# vaca1.edo_salud()
# vaca1.estado()

