class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Encapsular las propiedades
        # self.__nombre         = nombre
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
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        enemigo.vida = enemigo.vida - self.daño(enemigo)
        print(f'''{self.nombre} atacó a {enemigo.nombre} \n{self.nombre} realizó {self.daño(enemigo)} pts. de daños''')        
        if enemigo.esta_vivo():
           print(f'La vida de {enemigo.nombre} es {enemigo.vida}')
        else:
            enemigo.vida = 0
            print(f'{enemigo.nombre} ha muerto')



    # # Acceder al atributo
    # def get_fuerza(self):
    #     return self.__fuerza    
    # # Modificar al atributo previamente encapsulado
    # def set_fuerza(self, fuerza):
    #     if self.__fuerza > 0:
    #         self.__fuerza = fuerza
    #     else:
    #         self.__fuerza = 0
        
    # def get_atributos(self):
    #     return self.__atributos()

# Herencia
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    def cambiar_arma(self):
        opcion = int(input('Elige un arma: (1) Acero Valyrio, daño 8. (2) Espada Matadragones, daño 10: '))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Opción no valida')
    def atributos(self):
        super().atributos()
        print(f'· Espada:       {self.espada}')
        
    def daño(self, enemigo):
        return (self.fuerza * self.espada) - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    def atributos(self):
        super().atributos()
        print(f'· Libro:        {self.libro}')
        
    def daño(self, enemigo):
        return self.libro * self.inteligencia - enemigo.defensa
        
def combate(personaje_1, personaje_2):
    turno = 1
    while personaje_1.esta_vivo() and personaje_2.esta_vivo():
        print(f'\nTurno {turno}')
        personaje_1.atacar(personaje_2)
        personaje_2.atacar(personaje_1)
        turno += 1
    if personaje_1.esta_vivo():
        print(f""" \n{personaje_1.nombre} ganó. \n{personaje_1.nombre} le quedaron {personaje_1.vida} pts de vida""")
    else:
        print(f""" \n{personaje_2.nombre} ganó. \n{personaje_2.nombre} le quedaron {personaje_2.vida} pts de vida""")


def run():
    personaje_1 = Personaje('Guts',10,5,3,1000)
    personaje_2 = Mago('Vanessa',2,10,2,1000,5)
    personaje_2.atributos()
    combate(personaje_1, personaje_2)
    
    
if __name__ == '__main__':
    run()
    

