print("Programa de evaluación de notas de alumno")

#la funcion input permite parametros
nota_alumno = input()

#funcion 
def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "suspendido"
		calificacion = 7
	return valoracion

print(evaluacion(float(nota_alumno)))

print("Adios!")


