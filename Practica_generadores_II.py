#aqui veremos la instruccion yield from
#cuando se coloca un * antes del parametro le estamos indicando que va a recibir
#un número indeterminado de elementos y los va a recibir en tupla.
def devuelve_ciudades(*ciudades):
	#bucle for padre
	for elemento in ciudades:
	
	#bucle for anidado
		#for subelemento in elemento:
		
		#variable yield from
			yield from  elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

#utilizamos la funcion next
print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
