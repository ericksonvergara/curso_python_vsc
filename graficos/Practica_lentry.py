#metodo entry
from tkinter import *
'''
raiz = Tk()

miFrame=Frame(raiz, width= 1200, height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.place(x=100, y=100)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.place(x=100, y=100)


raiz.mainloop()
'''

#metodo grid(row= 0, colum= 0)

raiz = Tk()

miFrame=Frame(raiz, width= 1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="green", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

#para alinear los textos utilizamos el metodo Sticky
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

DireccionLabel=Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text="password:")
passwordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
#metodo pad padx - pady
#para cambiar el color del texto y la alinacion trabajamos el metodo config
# fg - justify
raiz.mainloop()