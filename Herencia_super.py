class Persona():
    def __init__(self, nombre, edad, direccion):

        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def descripcion(self):

        print("nombre: ", self.nombre, "Edad: ", self.edad, "Direccion: ", self.direccion )

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, direccion_empleado):

        super().__init__(nombre_empleado, edad_empleado, direccion_empleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        
        super().descripcion()

        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

#creando objeto de tipo empleado
manuel = Persona("manuel", 55, "Colombia")

manuel.descripcion()

#instanciando un objeto de una clae
print(isinstance(manuel, Empleado))