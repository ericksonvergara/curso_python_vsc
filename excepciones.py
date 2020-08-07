#Son errores que ocurren durante la ejecucion del programa

def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def miltiplica(num1, num2):
	return num1 * num2

def division(num1, num2):

#fucnion para seguir las lineas de codigo asi suceda una exepcion	
	try:
		return num1 / num2
	
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return("Operacion errónea")
	
#capturando exepciones 
while True:
	
	try:
		op1 = (int(input("introduce el primer numero: ")))

		op2 = (int(input("introduce el segundo numero: ")))

		break

	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion = input("Introducir la operacion a realizar(suma, resta, multplica, division)")

if operacion == "suma":
		print(suma (op1, op2))

elif operacion == "resta":
		print(resta (op1, op2))

elif operacion == "multiplica":
		print(multiplica(op1, op2))

elif operacion == "division":
		print(division(op1, op2))
else:
	print("Operacion no contemplada")

print("Operacion ejecutasa. Continuacion de ejecucionel programa")

