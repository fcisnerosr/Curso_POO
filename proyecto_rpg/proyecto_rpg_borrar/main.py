import os
os.system('clear')

class Personaje():
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def estadisticas(self):
        print(f'  {self.nombre}')
        print(f'· fuerza = {self.fuerza}')
        print(f'· inteligencia = {self.inteligencia}')
        print(f'· defensa = {self.defensa}')
        print(f'· vida = {self.vida}')

    def subir_nivel(self, fuerza):
        self.fuerza = self.fuerza + fuerza        
    
    def esta_vivo(self):
        return self.vida > 0
        # if self.vida > 0:
        #     # print(f'{self.nombre} esta vivo')
        #     return True

    def morir(self):
        self.vida = 0
        print(f'{self.nombre} murió')

    def daño(self, enemigo):
        return enemigo.defensa - self.fuerza
        # print(f'{self.nombre} le hizo daño a {enemigo.nombre}')

    def atacar(self, enemigo):
        self.vida = daño(self, enemigo)

heroe = Personaje('Link', 5, 3, 10, 100)
heroe.estadisticas()

villano = Personaje('Ganon', 15, 1, 10, 100)
villano.estadisticas()

# heroe.subir_nivel(5)
heroe.estadisticas()

print(heroe.esta_vivo())

print(heroe.daño(villano))
villano.estadisticas()