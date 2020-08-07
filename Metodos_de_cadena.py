#Metodos de cadenas
'''
nombreUsuario = input("Introduce un nombre de usuario: ")


print("El nombre de usuario es: " + nombreUsuario.upper())
print("El nombre de usuario es: " + nombreUsuario.lower())
print("El nombre de usuario es: " + nombreUsuario.capitalize())
'''

edad= input("Introduce la edad: ")

#print(edad.isdigit)

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numerico")

    edad = input("Introduce un valor numerico")

if (int(edad)<18):

    print("No puede pasar")
else:
    print("puede pasar")