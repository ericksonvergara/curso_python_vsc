'''
#Instruccion para imprimir horizontalmente
for i in ["pildoras", "informaticas", 3]:
	print ("hola", end = " ")

#Recorrer por caracter
for i in "ericksonvergararojas@hotmail.com":

	print("hola", end = " ")

'''
#ejemplo para comprobar la veracidad de un correo
'''
email = False

for i in "ericksonvergararojas@hotmail.com":
	
	if(i=="@"):
		email=True

if email == True:
	print("El email es correcto")
else:
	print("El email es incorrecto")
'''
#Ingresando direcccion de correo por teclado y verificarla
'''
contador = 0
miemail = input("Introduce tu direccion de e-mail:")

for i in miemail:
	
	if(i=="@" or i == "."):
		contador = contador+1
		

if contador == 2:
	print("El email es correcto")
else:
	print("El email es incorrecto")
'''
#Tipo range

for i in range(5):
	print (i)
