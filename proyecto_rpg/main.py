# import os
# os.system('clear')

# class personaje():
#     def __init__(self, nombre, fuerza, inteligencia, vida):
#         self.nombre = nombre
#         self.fuerza = fuerza
#         self.inteligencia = inteligencia
#         self.vida = vida
        
#     def atributos(self):
#         print(f'- Nombre: {self.nombre}')
#         print(f'- Fuerza: {self.fuerza}')
#         print(f'- Inteligencia: {self.inteligencia}')
#         print(f'- Vida: {self.vida}')
        
#     def subir_nivel(self, fuerza, inteligencia, vida):
#         self.fuerza = self.fuerza + fuerza
#         self.inteligencia = self.inteligencia + inteligencia
#         self.vida = self.vida + vida
        
#     def esta_vivo(self):
#         return self.vida > 0
    
#     def muerto(self):
#         print(f'{self.nombre} ha muerto') if self.vida <= 0 else print(f'{self.nombre} sigue vivo')
        
#     def daño(self, enemigo):
#         return enemigo.vida - self.fuerza
    
#     def dañado(self, enemigo):
#         self.vida = self.vida - enemigo.fuerza
        

# enemigo = personaje('Toño', 10, 10, 10)

# personaje1 = personaje('Paco', 5, 10, 0)
# personaje1.atributos()
# personaje1.subir_nivel(5, 0, -1)
# personaje1.atributos()
# print(personaje1.esta_vivo())
# personaje1.muerto()
# print(personaje1.daño(enemigo))
# enemigo.dañado(personaje1)
# enemigo.atributos()
# enemigo.muerto()


























import os
os.system('clear')

class Personaje():
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
    def atributos(self):
        print(f'- Nombre = {self.nombre}')
        print(f'- Vida = {self.vida}')
        print(f'- Ataque = {self.ataque}')
        print(f'- Defensa = {self.defensa}')
        
    def subir_nivel(self, incremento):
        self.ataque = self.ataque + incremento
        self.defensa = self.defensa + incremento
        
    def atacar(self, contrincante):
        contrincante.vida = contrincante.vida - self.ataque
        if contrincante.vida < 0:
            contrincante.vida = 0
        print(f'{self.nombre} ha hecho daño a {contrincante.nombre}')
        print(f'{contrincante.nombre} tiene {contrincante.vida} puntos de vida')
    
    def vida_o_muerto(self):
        if self.vida <= 0:
            print(f'{self.nombre} ha muerto')
        else:
            print(f'{self.nombre} sigue vivo')
    
heroe = Personaje('Link', 10, 5, 5)
heroe.atributos()
heroe.subir_nivel(1)
heroe.atributos()

villano = Personaje('Ganon', 10, 11, 10)
villano.atributos()
villano.atacar(heroe)

heroe.atributos()
heroe.vida_o_muerto()

heroe.atacar(villano)
villano.vida_o_muerto()

heroe.atributos()
villano.atributos()


