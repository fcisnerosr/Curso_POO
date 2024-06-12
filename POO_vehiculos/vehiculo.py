class Vehiculo():
    def __init__(self, tipo, modelo, color, presion_llantas, no_llantas, lim_adecuado_presion):
        self.tipo                   = tipo
        self.modelo                 = modelo
        self.color                  = color
        self.presion_llantas        = presion_llantas
        self.no_llantas             = no_llantas
        self.lim_adecuado_presion   = lim_adecuado_presion

    def movimiento(self, acelerar, frenar):
        if acelerar == 1:
            print(f'{self.tipo} está avanzando')
        elif frenar == 1:
            print(f'{self.tipo} está frenando')
        else:
            print(f'{self.tipo} está detenido')

    def ponchado(self):
        if self.presion_llantas == 0:
            print(f'Las {self.no_llantas} llantas no contienen aire')
        else:
            print(f'Las {self.no_llantas} llantas contienen aire')

    def presion_adecuada(self):
        if self.presion_llantas >= self.lim_adecuado_presion:
            print(f'{self.presion_llantas} es una presion adecuada')
        else:
            print(f'{self.presion_llantas} no es una presion adecuada')

