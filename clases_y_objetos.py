class Celular:
    def __init__(self, marca, model, camar):
        self.mar = marca
        self.model = model
        self.camar = camar
    
    def llamar(self):
        print(f"estas llamando desde un: {self.model}")
    def cortar(self):
        print(f"cortaste desde un: {self.model}")

celular1 = Celular('Samsung', 'S23', '48MP')
print(celular1.mar)

celular2 = Celular('Apple', 'iPhone 15 Pro', '48MP')
print(celular2.model)

celular1.llamar()