num1= int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))

def DevuelveMax(num1, num2):
	if num1 > num2:
		print(num1)
	elif num2 > num1:
		print(num2)
	else:
		print("Los número son iguales")

print("El número  mas alto es: ")

DevuelveMax(num1, num2)