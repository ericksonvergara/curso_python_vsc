import pickle

#codificando lista en codigo binario

'''
#creando lista

lista_nombre=["Pedro", "Ana", "Maria", "Isabel"]

#fichero con acceso de escritura binaria "wb"
fichero_binario=open("lista_nombre", "wb")

pickle.dump(lista_nombre, fichero_binario)

fichero_binario.close()

del(fichero_binario)
'''

#Rescatando el fichero

fichero=open("lista_nombre", "rb")

lista=pickle.load(fichero)

print(lista)