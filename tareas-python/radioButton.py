from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")
#Se logra configurar la raiz
root = Tk()

opcion = IntVar()

Radiobutton(root, text="Bueno", variable=opcion, 
            value=1, command=seleccionar).pack()
Radiobutton(root, text="Malo", variable=opcion, 
            value=2, command=seleccionar).pack()
Radiobutton(root, text="Pésimo", variable=opcion,   
            value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()


root.mainloop()