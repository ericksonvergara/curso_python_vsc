#como lanzar exepciones
import math
'''
def evaluaEdad(edad):

#Creando exepcion
	if edad < 0:
		#Instruccion de exepcion
		raise TypeError("No se permiten edades negativas")
	if edad < 20:
		return "Eres muy joven"
	elif edad < 40:
		return "Eres joven"
	elif edad < 65:
		return "Eres maduro"
	elif edad < 100:
		 return "Cuidate..."

print(evaluaEdad(-20))
'''
#Progrma para calcular una raiz cuadrada
def calculaRaiz(num1):
	if num1 < 0:
		#lanzando exepcion RAISE
		raise ValueError("El número no puede ser negativo")

	else:
		#la variable "math.sqrt" nos permite calcular la raiz cuadrada
		return math.sqrt(num1)

#Pidiendo al usuario que ingrese por teclado
op1 = (int(input("Introduce un número: ")))
try:
	print(calculaRaiz(op1))
except ValueError as Errordenúmeronegativo:
	
	print(Errordenúmeronegativo)


print("programa terminado")
	