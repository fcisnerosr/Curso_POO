import os; import datetime
os.system('clear')

now = datetime.datetime.now()
current_time = now.time()
print(now)

class Animal():
    def __init__(self, nombre,  genero, animal,salud, peso, ubicacion):
        self.nombre     = nombre
        self.genero     = genero
        self.animal     = animal
        self.salud      = salud        
        self.peso       = peso
        self.ubicacion  = ubicacion

    def estado(self):
        print(f'{self.animal.capitalize()}')
        print(f'· Nombre:       {self.nombre.capitalize()}')
        print(f'· Genero:       {self.genero}')
        print(f'· Salud:        {self.salud}')
        print(f'· Peso:         {self.peso} kg')
        print(f'· Ubicación:    {self.ubicacion}')

    def comer(self):
        self.alimento = input('Elije un alimento: manzana +1 kg, elote +2 kg: ')
        return self.alimento

    def ganar_peso(self):
        if self.ponte_a_pastar():
            self.peso = self.peso + 0.5
        elif self.alimento == 'manzana':
            self.peso = self.peso + 1
        elif self.alimento == 'elote':
            self.peso = self.peso +2

        # if self.alimento == 'manzana':
        #     self.peso = self.peso + 1
        # elif self.alimento == 'elote':
        #     self.peso = self.peso + 2
        
            

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
                self.ojos = 'despierta'
            else:
                print(f'{self.nombre} está despierto, no es hora de dormir')
                self.ojos = 'despierto'
        else:            
            if self.genero == 'hembra':
                print(f'{self.nombre.capitalize()} está dormida, no la molestes')
                self.ojos = 'dormida'
            else:
                print(f'{self.nombre.capitalize()} está dormido, no la molestes')
                self.ojos = 'dormido'

    def guardate(self):
        if self.ubicacion == 'cabaña':
            print(f'{self.animal} guardada')
        elif self.ubicacion == 'área verde':
            print(f'{self.animal} voy para allá')
            self.ubicacion = 'cabaña'
        else:
            print(f'{self.animal} está perdida')

    def ponte_a_pastar(self):
        if self.ojos == 'despierto' or self.ojos == 'despierta':
        # if current_time <= datetime.time(hour=4, minute=0, second=0) and self.ojos == 'despierto' or self.ojos == 'despierta':
            self.ganar_peso()
            self.estado()

    # def haz_popo():
    #     pass

    # def esta_vivo():
    #     pass



vaca1 = Animal('Lola', 'hembra', 'vaca', 100, 500, 'área verde')
vaca1.estado()
vaca1.descansa()
# vaca1.guardate()
# vaca1.comer()
vaca1.ponte_a_pastar()
vaca1.estado()
print(vaca1.ojos)

# vaca1.ganar_peso()
# vaca1.edo_salud()
# vaca1.estado()

