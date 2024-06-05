class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida) :
        self.nombre         = nombre
        self.fuerza         = fuerza
        self.inteligencia   = inteligencia
        self.defensa        = defensa
        self.vida           = vida

    def atributos(self):
        print(f'{self.nombre}:')
        print(f'· Fuerza:       {self.fuerza}')
        print(f'· Inteligencia: {self.inteligencia}')
        print(f'· Defensa:      {self.defensa}')
        print(f'· Vida:         {self.vida}')

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza         = self.fuerza + fuerza
        self.inteligencia   = self.inteligencia + inteligencia
        self.defensa        = self.defensa + defensa

    def esta_vivo(self):
        return self.vida >= 0
    
    def morir(self ):
        self.vida = 0
        print(f'{self.nombre} ha muerto')

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        enemigo.vida = enemigo.vida - self.daño(enemigo)
        print(f'{self.nombre} atacó a {enemigo.nombre}')
        if not enemigo.esta_vivo():
            enemigo.morir()
        else:
            print(f'La vida de {enemigo.nombre} es {enemigo.vida}')


        


