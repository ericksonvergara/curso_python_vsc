#controlar acceso a mayores de edad
print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad:"))

if edad_usuario < 18:
	print("No puedes pasar")
elif edad_usuario > 150:
	print("Edad incorrecta")
else:
	print("Siga")
print("")
print("El programa ha finalizado")

print("--------------------------------------------------")

nota_alumno = int(input("Introduce tu nota, por favor: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("suficiente")
elif nota_alumno<7:
	print("bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")
