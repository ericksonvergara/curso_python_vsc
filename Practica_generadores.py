#generadores
#sintaxis de un generador
# def generanumeros():
#		--------
#	   yield numeros

def generaPares(limite):
	numero = 1
	

	while numero < limite:

		yield numero * 2
		
		numero = numero + 1

#creando variable objeto

devuelvePares = generaPares(10)

for i in devuelvePares:

	print(i)

#imprimiendo elementos en concreto

def generaPares2(limite):
	numero = 1
	

	while numero < limite:

		yield numero * 2
		
		numero = numero + 1

#creando variable objeto

devuelvePares = generaPares2(10)

print(next(devuelvePares))

print("Aqui podria ir mas codigo....")

print(next(devuelvePares))

