import os
from Personaje import Personaje
from Personaje import Guerrero
from Personaje import Mago
os.system('clear')

heroe   = Personaje('Link',     10, 1, 5, 100)
enemigo = Personaje('Ganon',    10, 1, 2, 2)

# heroe.atacar(enemigo)
# enemigo.atributos()
# heroe.atributos()

# guts = Guerrero('Guts', 20, 5, 10, 10, 8)
# guts.cambiar_arma()
# print(guts.espada)
# guts.atributos()

# el_mago = Mago('Merlin', 1, 10, 2, 2, 10)
# el_mago.atributos()

goku = Personaje('Goku', 25, 2, 10, 100)
goku.atributos()
cloud = Guerrero('Cloud', 10, 3, 15, 100, 20)
cloud.atributos()
merlin = Mago('Merlin', 5, 18, 5, 100, 18)
merlin.atributos()