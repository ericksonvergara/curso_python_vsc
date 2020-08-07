import pickle

class Vehiculo(): #cracion de una clase

    #creacion de constructor de la clase
    def __init__(self, marca, modelo):

        #creando atributos
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera =True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca ", self.marca, "\nModelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frena)

#creando objeto
coche1=Vehiculo("Mazda", "MX5")

coche2 = Vehiculo("Seat","Leon")

coche3 = Vehiculo("Renault", "Megane")

coches=[coche1, coche2, coche3]

fichero=open("los coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

'''
#rescatando el archivo

ficheroApertura=open("los coches", "rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:

    print(c.estado())
'''
