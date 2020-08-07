#En este programa evaluaremos los siguientes requisitos
#para poder acceder a una beca

print("Programa de becas año 2020")

#creacion de variables
distancia_escuela = int(input("Introduce la distancia de su casa a la escuela en Kms: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos en la institucion: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto: "))

#Operadores and, or
if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No Tienes derecho a beca")

print("<--------------------------------------------------------->")

# Operador in
print("Asignaturas optativas año 2020")

print("Asignaturas optaivas: Informatica grafica - pruebas de software - usabilidad y accesibilidad")

opcion = input("Escribe la Asignatura escogida: ")

#convirtiendo el codigo en minusculas "lower"
asignatura = opcion.lower()

if asignatura in ("Informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura elegida no esta contemplada")



