import math
#bucle While
#sintaxis 
# while condicion:
#	  cuerpo del bucle
'''
i = 1

while i <= 10:
	print("Ejecucion " + str(i))
	i = i + 1
print("Termno la ejecución")
'''

#progrma donde introducimos la edad 
'''
edad = int(input("Introduce tu edad: "))


while  edad < 0:
	print("Has introducido una edad negativa. vuelva a intentar")
	edad = int(input("Introduce tu edad por favor: "))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: "+ str(edad))	
'''
'''
while edad<5 or edad>100:
	print("Has introducido una edad incorrecta. vuelva a intentar")
	edad = int(input("Introduce tu edad por favor: "))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: "+ str(edad))
'''
#como hacer que un bucle no sea infinito

print("Programa de calculo de raiz cuadrada")

numero = int(input("Introduce un número:"))

intentos = 0

while numero < 0:
	print("no se puede hallar la raiz de un númeor negativo")

	if intentos ==2:
		print("has realizado demasiados intentos. El pr ha finalizado")
		break;
	numero = int(input("introducir un número por favor: "))
	if numero < 0:
		intentos = intentos + 1

if intentos < 2:
	solucion=math.sqrt(numero)
	print("la raiz cuadrada de ", numero, " es ", str(solucion))