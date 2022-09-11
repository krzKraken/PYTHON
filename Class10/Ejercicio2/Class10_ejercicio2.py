# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter
import sys


window = tkinter.Tk()

# window conf
window.columnconfigure(0, weight=2)
window.rowconfigure(0, weight=1)

opciones = ["opcion 1", "opcion 2", "opcion 3", "opcion 4", "opcion 5", "opcion 6"]
lista_opciones = tkinter.StringVar(value=opciones)

label = tkinter.Label(window, text="Escoja una opcion")
label.grid(column=0, row=0, padx=10, pady=10)

listbox = tkinter.Listbox(window, listvariable=lista_opciones, height=0)
listbox.grid(column=0, row=1, padx=10, pady=10)


window.mainloop()
sys.exit()
