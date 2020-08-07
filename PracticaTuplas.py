#tuplas
#las tuplas van entre parentesis(), aunque no es obligacion crearlas entre parentesis


#creando una tupla
mitupla=("Erickson", 11, 10, 1991)

#creando lista
milista2=["Erickson", "Vergara", "Rojas"]
#accediendo a un elemento en concreto de la tupla
print(mitupla[2])

#metodos para convetir metodos en tuplas
milista = list(mitupla)

print(milista)

#converti de lista a tupla
mitupla3 = tuple(milista2)
print(mitupla3)

#comprobar si el elemento exite en la tupla
print("Erickson" in mitupla3)

#averiguando cuantos elementos se encuentra en una tuplas
print(mitupla3.count("Vergara"))

#averiguando la longitud de una tupla
print(len(mitupla3))

#tuplas unitarias Lleva el elemento siempre acompañado de una "coma"
mitupla5=("weimar",)
print(len(mitupla5))

#empaquetado de tupla
mitupla6 = ("daniel", 1, 5, 2002)
nombre, dia, mes, agno = mitupla6
print(nombre)
print(dia)
print(agno)
print(mes)

#como realizar una busqueda en una tupla
print(mitupla6.index("daniel"))