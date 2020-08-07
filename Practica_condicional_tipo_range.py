#tipo range
for i in range(5, 50, 3):
	print(f"valor de la variable {i}")


#e-mail com range

valido = False

email=input("Introduce tu e-mail: ")

for i in range(len(email)):
	if email[i] == "@":

		valido = True

if valido:
	print("El e-mail es correcto")
else:
	print("e-mail incorrecto")


