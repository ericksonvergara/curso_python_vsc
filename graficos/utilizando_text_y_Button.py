#utilizando text y Button

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

#con esto sabemos que se trata de una cadena de caracteres
minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="green", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

#agregando margen al text
cuadrocomentario=Text(miFrame, width=20, height= 5)
cuadrocomentario.grid(row=4, column=1, padx=10, pady=10)

#creando scroll
scrollvert=Scrollbar(miFrame, command=cuadrocomentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")

#acomodando el scroll 
cuadrocomentario.config(yscrollcommand=scrollvert.set)

#para alinear los textos utilizamos el metodo Sticky
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

DireccionLabel=Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text="password:")
passwordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#agreagnco boton
#creamos una variable

def codigoBoton():
    minombre.set("Erickson")

boton=Button(raiz, text="Enviar", command=codigoBoton)
boton.pack()

#agregando instrucciones al boton
#boton=Button(raiz, text="Enviar")

#metodo pad padx - pady
#para cambiar el color del texto y la alinacion trabajamos el metodo config
# fg - justify
raiz.mainloop()