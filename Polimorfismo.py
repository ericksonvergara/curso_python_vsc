class coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

'''
#Creando una instancia de la clase moto
mivehiculo = Moto()
mivehiculo.desplazamiento()
mivehiculo2 = Camion()
mivehiculo2.desplazamiento()
mivehiculo3 = coche()
mivehiculo3.desplazamiento()
'''

#Polimorfismo
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo = Moto()
desplazamientovehiculo(mivehiculo)

