#Construccion de una clase = palabra reservada "class" y el nombre dela clase

class coche():
	
	#Creando constructor de la clase
	def __init__(self):

	#propiedades
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 #encapsulando una clase. para encapsular colocamos 2 guiones bajos
		self.__enmarcha=False

#estableciendo comportamientos

#un metodo e una funcion especial que pertenece a la clase
#una funcion no pertenece a ninguna clase	
#self es un parametro por defecto que hace referencia al propio objeto perteneciente a la clase

#creando un metodo
#Accediento al comportamiento del metodo
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo = self.chequeo_interno()

		if (self.__enmarcha and chequeo):
			
			return "El coche esta enmarcha"

		elif(self.__enmarcha and chequeo == False):
			return"Algo ha ido mal en el proceso, no podemos arrancar"

		else:
			return "El coche esta parado"

		#self. enmarcha = True


	def estado(self):
		print("El coche tiene " , self.__ruedas, " ruedas. un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
			
	
	def chequeo_interno(self):
		print("Realizando chequeo interno")	

		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

			return True
		else:
			return False
	#construyendo objetos de la clase

	#aqui realizamos una instanciacion de la clase

miCoche = coche() 

print(miCoche.arrancar(True))

miCoche.estado()

print(miCoche.chequeo_interno())

print("-------------------Acontinuacion creamos el segundo objeto------------------------")

miCoche2 = coche()#Instancia


print (miCoche2.arrancar(False))

miCoche2.estado()

print(miCoche2.chequeo_interno)