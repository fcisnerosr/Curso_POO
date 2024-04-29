class Animal():
    def comer(self):
        print('como porque soy animal')

class Mamifero():
    def amamantar(self):
        print('amamanto porque soy mamifero')

class Ave():
    def volar(self):
        print('vuelo porque soy ave')
    
class Murcielago(Animal, Mamifero, Ave):
    # pass
    def comer(self):
        super().comer()
        # print('Como porque soy murcielago')
        
batman = Murcielago()
batman.comer()
batman.volar()
batman.amamantar()