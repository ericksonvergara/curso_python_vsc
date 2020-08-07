#Nota:en python se pueden agregar variable de fierentes tipo en las listas

#crear lista
miLista=["erickson", "pepe", "maria", "martha"]

miLista2=["luisa", "rafael"]


print("------------------------------------------")
#agregar elemento al final de la lista
miLista.append("sandra")

#agregar elemento en x posicion de la lista
miLista.insert(2, "kevin")

#agregar varios elementos a la lista
miLista.extend(["juan", "daniel", "weimar"])

#eliminar elementos
miLista.remove("daniel")

#eliminar el ultimo elemento de la lista
miLista.pop()

#sumado listas
miLista3 = miLista+miLista2

print(miLista3[:])

#multiplicando listas
miLista4=["jorge", 5, True, 78.35]*3

print(miLista4)

#comprobar si un elemento existe o no en la lista
print("pepe" in miLista)

#devolver indice de la lista
print(miLista.index("erickson"))

#imprimir los elementos de la lista
print(miLista[:])


#imprimir x elemetos de la lista
print(miLista[1:4])
