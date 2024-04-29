class Gato():
    def sonido(self):
        return 'miau'
    
class Perro():
    def sonido(self):
        return 'guau'
    
gato1 = Gato()
perro1= Perro()

print(gato1.sonido())
print(perro1.sonido())

def hacer_sonido(animal):
    print(animal.sonido())
    
hacer_sonido(gato1)