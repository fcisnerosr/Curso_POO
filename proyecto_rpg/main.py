import os
from Personaje import Personaje
os.system('clear')

heroe   = Personaje('Link', 10, 1, 5, 100)
enemigo = Personaje('Ganon', 10, 1, 2, 2)

heroe.atacar(enemigo)
enemigo.atributos()
heroe.atributos()