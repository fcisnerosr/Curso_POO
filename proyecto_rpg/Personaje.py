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
        return self.vida >= 0
    
    def morir(self):
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
        
def run():
    # heroe = Personaje('Link', 10, 3, 2, 100)
    # villan= Personaje('Ganondorf', 10, 3, 2, 100)
    # villan.atributos()
    # heroe.atributos()
    # villan.atacar(heroe)
    # heroe.atributos()
    # guts = Guerrero('Guts', 10, 3, 2, 100, 0)
    # gotan = Personaje('Gotan', 10, 2, 1, 100)
    # gotan.atributos()
    # guts.cambiar_arma()
    # guts.atributos()
    # guts.daño(gotan)
    # print(guts.fuerza)    
    # guts.atacar(gotan)
    # gotan.atributos()
    sayayin = Personaje('Goku', 20, 15, 10, 100)
    sayayin.atributos()
    link    = Guerrero('Link', 20, 15, 10, 100, 5)
    link.atributos()
    merlin  = Mago('Merlin', 20, 15, 10, 100, 5)
    merlin.atributos()
    sayayin.atacar(link)
    link.atacar(merlin)
    merlin.atacar(sayayin)
    
    
if __name__ == '__main__':
    run()
    

