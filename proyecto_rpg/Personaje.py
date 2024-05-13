class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida) :
        self.nombre       = nombre
        self.fuerza         = fuerza
        self.inteligencia = inteligencia
        self.defensa       = defensa
        self.vida             = vida

    def atributos(self):
        print(f'{self.nombre}:')
        print(f'- Fuerza: {self.fuerza}')
        print(f'- Inteligencia: {self.inteligencia}')
        print(f'- Defensa: {self.defensa}')
        print(f'- Vida: {self.vida}')

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida >= 0
    
    def morir(self ):
        self.vida = 0
        print(f'{self.nombre} ha muerto')

    def daño(self, contrincante):
        return self.fuerza - contrincante.defensa
    
    def atacar(self, contrincante):
        daño = self.daño(contrincante)
        contrincante.vida = contrincante.vida - daño
        print(f'{self.nombre} hizo {daño} puntos de daño a {contrincante.nombre}')
        if contrincante.esta_vivo():
            print(f'{contrincante.nombre} tiene {contrincante.vida} de vida')
        else:
            contrincante.morir()
