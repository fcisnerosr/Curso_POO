import os
from Personaje import Personaje
os.system('clear')

mi_personaje = Personaje('Link', 10, 1, 5, 100)
mi_personaje.atributos()
mi_enemigo = Personaje('Ganon', 15, 1, 5, 2)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()