from tkinter import *

root=Tk()

varOpcion=IntVar()

#como rescatar los valores que se pulsaron

def imprimir():

    #print(varOpcion.get())
    if varOpcion.get()== 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otra opcion")

Label(root, text="Genero").pack()

Radiobutton(root, text="masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="femenino", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()


root.mainloop()