class Operacion_basica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def operacion(self):
        c = self.a + self.b
        print(c)
        
class Operacion_avanzada(Operacion_basica):
    def __init__(self, a, b):
        super().__init__(a,b)
    def operacion(self):
        c = self.a ** self.b
        print(c)
        
class Raiz(Operacion_basica):
    def __init__(self, a, b):
        super().__init__(a, b)
    def raiz(self):
        c = self.a ** (1/self.b)
        print(c)
        
class Vector(Operacion_basica):
    def __init__(self, a, iter):
        super().__init__(a)
        self.iter = iter
                
    def arma_vector(self):
        V = [num * self.a for num in iter]
        print(V)
        
operacion1 = Operacion_avanzada(2, 3)
operacion1.operacion()
operacion2 = Operacion_basica(3, 10)
operacion2.operacion()
operacion3 = Raiz(81, 2)
operacion3.raiz()
iter = [1, 2, 3, 4, 5]
operacion4 = Vector(2, iter)
operacion4.arma_vector()

# class A:
#     def hablar(self):
#         print('Hola desde A')
        
# class B:
#     def hablar(self):
#         print('Hola desde B')
        
# class C(A):
#     def hablar(self):
#         print('Hola desde C')
        
# class D(B, C):
#     pass

# objet = D()
# objet.hablar()