import pickle

#creando clase

class Persona:

    #Constructor de la case
    def __init__(self, nombre, edad, genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        print("se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listapersonas:


    personas=[]

    #Creando un constructor
    def __init__(self):

        listadepersonas=open("ficheroExterno", "ab+")
        
        #despalazando el cursor al inicio
        listadepersonas.seek(0)

        try:
            self.personas=pickle.load(listadepersonas)
            print("se cargaron {} perosnas del fichero externo".format(len(self.personas)))

        except:
            print("el fichero esta vacio")

        finally:
            listadepersonas.close()
            del(listadepersonas)
    
    #creando metodo
    def agregarpersonas(self, p):
        self.personas.append(p)
        self.guardarpersonasenficheroexterno()
    #creando metodo
    def mostrarpersonas(self):
        for p in self.personas:
            print(p)

    def guardarpersonasenficheroexterno(self):
        listapersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listapersonas)
        listapersonas.close()
        del(listapersonas)

    #metodo para leer la lista despues de cargados
    def mostrarinfoficheroexterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        #recorremos con el for lo cargado en la lista
        for p in self.personas:
            print(p)

#insrancia de la clase
milista=listapersonas()

persona=Persona("sandra","femenino",29)
milista.agregarpersonas(persona)
#mostrando la informacion utilizando la instancia
milista.mostrarinfoficheroexterno()
'''
p=Persona("sandra", "femenino", 28)
milista.agregarpersonas(p)
milista=listapersonas()
p=Persona("aantonio", "masculino", 18)
milista.agregarpersonas(p)
milista=listapersonas()
p=Persona("ana", "femenino", 19)
milista.agregarpersonas(p)

milista.mostrarpersonas()
'''

