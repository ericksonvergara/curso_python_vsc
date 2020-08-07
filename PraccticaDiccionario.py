#Diccionarios

#A difrenecia de las tuplas y las listas los diccionarios van en "llaves"
#Los diccionarios permiten variables de todo tipo
#creando diccionario
midiccionario = {"Alemania" : "Berlin", "Francia":"Paris", "Reino unido":"Londres", "España":"Madrid", "Colombia":"Bogota"}

midiccionario2 = {"Argentina":"buenos Aires", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)

#acceder al diccionario entero
print(midiccionario)

#Consultando diccionario
print(midiccionario["Francia"])
print(midiccionario["España"])

#agregar elemento al diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#corregir un elemento del diccionario
midiccionario["Italia"]="Roma"
print(midiccionario)

#Como eliminar elementos del diccionario
del midiccionario["Reino unido"]
print(midiccionario)

#Utilizando tuplas para asignar claves a los valores
mitupla=["uruguay", "paraguay", "Ecuador", "chile"]
midiccionario3 = {mitupla[0]:"Montevideo", mitupla[1]:"Asuncion", mitupla[2]:"Quito", mitupla[3]:"Santiago"}
print(midiccionario3)
print(midiccionario3["paraguay"])

#como hacer que un diccionario almacene un tupla
midiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario4)
print(midiccionario4["anillos"])

#como guardar un diccionario demtro de otro diccionario
midiccionario5={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario5)

#como obtener las claves, los valores y la longitud del diccionario

print(midiccionario5.keys())
print(midiccionario5.values())
print(len(midiccionario5))