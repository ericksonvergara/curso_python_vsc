from tkinter import *

#construccion de raiz
raiz=Tk() 

#dandole titulo a la ventana
raiz.title("Ventana de Pruebas")

#impedir que se redireccione un aventana
raiz.resizable(0, 0)

#cambiando el icono de ventana
raiz.iconbitmap("python.ico")

#cambiando el tamaño de la ventana
raiz.geometry("650x350")

#cambiar color de fondo
raiz.config(bg="green")



raiz.mainloop()