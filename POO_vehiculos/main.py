import os 
from vehiculo import Vehiculo
from vehiculo import Automovil
from vehiculo import Bicicleta
os.system('clear')

mi_carro = Automovil('automovil', '2012', 'gris', 10, 4)
mi_carro.movimiento(1,0)
mi_carro.presion_adecuada()
mi_carro.ponchado()

mi_bici = Bicicleta('bicicleta', '2020', 'roja', 50, 2)
mi_bici.movimiento(0,1)
mi_bici.movimiento(0,0)
mi_bici.presion_adecuada()
mi_bici.ponchado()

