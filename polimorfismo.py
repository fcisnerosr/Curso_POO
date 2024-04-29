class Gato():
    def sonido(self):
        return 'miau'
    
class Perro():
    def sonido(self):
        return 'guau'

# Definición de objetos
gato1 = Gato()
perro1= Perro()

# polimorfismo de métodos
print(gato1.sonido())
print(perro1.sonido())


# polimorfismo de funcion
def hacer_sonido(animal):
    print(animal.sonido())
    
hacer_sonido(gato1)
hacer_sonido(perro1)