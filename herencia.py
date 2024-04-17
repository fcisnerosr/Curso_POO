class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f'hola soy {self.nombre}')
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        print('Hola, soy un empleado')
        
empleado1 = Empleado('Juan Diego', 32, 'mexicano', 'ingeniero civil', '25 mil pesos')
print(empleado1.nombre)
print(empleado1.salario)
empleado1.hablar()
