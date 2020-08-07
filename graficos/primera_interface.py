from tkinter import *

#construccion de raiz
raiz=Tk() 

#dandole titulo a la ventana
raiz.title("Ventana de Pruebas")

#impedir que se redireccione un aventana
#raiz.resizable(0, 0)

#cambiando el icono de ventana
raiz.iconbitmap("python.ico")

#cambiando el tamaño de la ventana
#raiz.geometry("650x350")

#cambiar color de fondo
raiz.config(bg="green")

#creando el frame
miframe=Frame()

#metiendo el frame dentro de la raiz
miframe.pack()

#cambiando el comportamiento por defecto del frame
miframe.pack(side="right", anchor="n")

miframe.pack(fill = "y", expand=True)

#dandole color al frame
miframe.config(bg= "red")

miframe.config(bd = 35)

#cambiando el borde
#miframe.config(relief="groove")

#miframe.config(relief="sunker")

miframe.config(cursor="pirate")


#denadole tamaño al frame
miframe.config(width = 650, height= 350)

#cambiando el icono del icono del cursos






raiz.mainloop()