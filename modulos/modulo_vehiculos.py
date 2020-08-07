#creacion de la clase
class vehiculos():

    #constructor de la clase
    def __init__(self, marca, modelo):
        
        #caracteristicas del constructor
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    #comportamientos del objeto
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"
#Sintaxis para heredar
class Moto(vehiculos):
    #Creando comportamiento de la moto
    hcaballito = ""
    
    #medoto caballito
    def caballito(self):
        self.hcaballito="voy haciendo caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VElectricos(vehiculos):
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)
        
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

