#Condicionales

edad = 7

if 0 < edad < 100:
	print("la edad es correcta")
else:
	print("edad incorrecta")

print("<-------------------------------------------------------->")

salario_presidente = int(input("Introduce el salario del presidente: "))

#concatenacion de caracteres
print("salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))

#concatenacion de caracteres
print("salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))

#concatenacion de caracteres
print("salario Jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del administrativo: "))

#concatenacion de caracteres
print("salario del administrativo: " + str(salario_administrativo))

# Concatenaciom de operadores de comparacion
if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")
