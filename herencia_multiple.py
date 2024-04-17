class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f'hola soy {self.nombre}')
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad        
    def mostrar_habilidad(self):
        print(f'mi habilidad es: {self.habilidad}, y me llamo {self.nombre}. Tengo {self.edad} y soy {self.nacionalidad}.')

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        print(f'{super().mostrar_habilidad()}')
  
empleadoartista1 = EmpleadoArtista('David', 32, 'mexicano', 'pintar', '15 mil pesos mexicanos', 'IVEC')
empleadoartista1.mostrar_habilidad()
empleadoartista1.hablar()
