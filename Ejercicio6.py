email=input("Introduce tu e-mail: ")

contador_arroba = 0
contador_punto = 0
for i in range(len(email)):
	if email[i] == "@":
		contador_arroba = contador_arroba + 1
	
	if email[i] == ".":
		contador_punto = contador_punto + 1

if contador_punto == 0 or contador_arroba != 1:
	print("El e-mail es incorrecto")
else:
	print("e-mail correcto")