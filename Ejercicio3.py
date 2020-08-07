num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

def media(num1, num2, num3):
	promedio = (num1 + num2 + num3) / 3
	print (promedio)
print("El promedio de los numero ingresados es: ")

media(num1, num2, num3)