class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentar(self):
        return print(f'Mi nombre es {self.nombre} y mi edad es {self.edad}')
              
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__( nombre, edad)
        self.grado = grado
    def presentarse(self):
        print(f'Mi nombre es {self.nombre} y mi grado es {self.grado}')
        
estudiante1 = Estudiante('Aldo', 11, '4°')
estudiante1.presentarse()

estudiante2 = Estudiante('Paco', 12, '6°')
estudiante2.presentarse()

persona1 = Persona('Claudia', 22)
persona1.presentar()
        
            