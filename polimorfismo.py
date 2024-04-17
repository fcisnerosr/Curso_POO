class Gato():
    def sonido(self):
        print('miau') 
        
class Perro():
    def sonido(self):
        print('guau')

def hacer_sonido(animal):
    return animal.sonido()
    
    
    
animal1 = Gato()
# animal1.sonido()

animal2 = Perro()
# animal2.sonido() # polimorfismo: mismo método diferente objeto

hacer_sonido(animal1)
hacer_sonido(animal2)