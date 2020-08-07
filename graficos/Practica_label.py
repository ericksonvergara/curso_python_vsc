#sintaxis para utilizar un label
#variable = label(contenedor, opciones)
from tkinter import *

#creacion de la raiz
root=Tk()

miFrame=Frame(root, width = 500, height = 400)

#empaquetando

miFrame.pack()

miImagen=PhotoImage(file="escudo.png")

miLabel= Label(miFrame, text="hola alumnos de python")
miLabel.place(x=100, y=200)

#abreviar sintaxis label
Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()
