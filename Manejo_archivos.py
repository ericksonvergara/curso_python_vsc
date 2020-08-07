from io import open

#Creando archivo externo
'''
archivo_texto = open("archivo.txt", "w")

frase = "estupendo dia para estudiar Python \n el miercoles"

archivo_texto.write(frase)

archivo_texto.close()
'''
#como abrir un archivo en modo lectura
'''
archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)
'''

#abriando archivo en modo lectura en firma de lista
'''
archivo_texto=open("archivo.txt", "r")

lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[1])
'''
#archivo para agregar informacion
'''
archivo_texto = open("archivo.txt","a")
archivo_texto.write("\n siempre es una buena ocacion para estudiar Python")
archivo_texto.close()
'''
#abriendo o leyendo archivo de texto
'''
archivo_texto=open("archivo.txt", "r")
print(archivo_texto.read())
'''
'''
#como posicionar un puntero con seek()
archivo_texto=open("archivo.txt", "r")
#print(archivo_texto.read())
#archivo_texto.seek(len(archivo_texto.read())/2)
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
'''
#lectura y escritura

archivo_texto = open("archivo.txt","r+")

archivo_texto.write("hola")

#print(archivo_texto.readline())
lista_texto=archivo_texto.readlines();
lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()