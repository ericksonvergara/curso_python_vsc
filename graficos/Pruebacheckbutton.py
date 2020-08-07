from tkinter import *

root=Tk()

root.title("Ejemplo")

foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa").pack()
Checkbutton(root, text="Montaña").pack()
Checkbutton(root, text="Turismo rural").pack()

root.mainloop()