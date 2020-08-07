#Ejercicio password

password = input("Ingrese la contraseña: ")

contador = 0

for i in range(len(password)):
	
	if password[i] == " ":

			contador = 1

if len(password)<8 or contador>0:
	print("Contraseña incorrecta")
else:
	print("Contraseña correcta") 
	