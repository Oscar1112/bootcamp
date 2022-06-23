from cgitb import reset
import tkinter
from tkinter import StringVar, ttk





window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
selected = tkinter.StringVar()

radio1 = ttk.Radiobutton(window, text="si", value="1", variable=selected)
radio2 = ttk.Radiobutton(window, text="opción2", value="2", variable=selected)
Buttom = ttk.Button(window, text="Reiniciar", value="3", variable=selected, command=reset)
#Pocisionamiento
radio1.grid(column=0, row=1, padx=10, pady=10)
radio2.grid(column=0, row=2, padx=10, pady=10)
Buttom.grid(column=0, row=3, padx=10, pady=10)
window.mainloop()
