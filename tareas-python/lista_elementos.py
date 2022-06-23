import tkinter


window = tkinter.Tk()
saludo = tkinter.Label(window, text="Seleccione una carrera", bg="pink")
#WINDOW COLUMN


elementos = ["Derecho", "Medicina", "Idiomas", "Economia"]
elementoss = tkinter.StringVar(value=elementos)
listbox= tkinter.Listbox(window, height=50, listvariable=elementoss)

saludo.pack()
listbox.pack(ipadx=60, ipady=40)


window.mainloop()