# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

import sys
import tkinter

window = tkinter.Tk()

window.columnconfigure(0, weight=2)
window.rowconfigure(0, weight=2)

frame1 = tkinter.Frame(window, width=500, height=300, relief="sunken")
frame1.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
label = tkinter.Label(frame1, text="Lista de radioButton")
label.grid(column=0, row=0, padx=10, pady=10)
seleccionado = tkinter.IntVar()


def setValor():

    label_seleccionado.config(text=f"Opcion seleccionada: {seleccionado.get()}")


def resetSeleccion():
    label_seleccionado.config(text=f"Opcion seleccionada:  ")
    seleccionado.set(None)


rb1 = tkinter.Radiobutton(
    frame1, text="opcion 1", value=1, variable=seleccionado, command=setValor
)
rb2 = tkinter.Radiobutton(
    frame1, text="opcion 2", value=2, variable=seleccionado, command=setValor
)
rb3 = tkinter.Radiobutton(
    frame1, text="opcion 3", value=3, variable=seleccionado, command=setValor
)
rb4 = tkinter.Radiobutton(
    frame1, text="opcion 4", value=4, variable=seleccionado, command=setValor
)
rb5 = tkinter.Radiobutton(
    frame1, text="opcion 5", value=5, variable=seleccionado, command=setValor
)
rb1.grid(column=0, row=1, padx=5, pady=5)
rb2.grid(column=0, row=2, padx=5, pady=5)
rb3.grid(column=0, row=3, padx=5, pady=5)
rb4.grid(column=0, row=4, padx=5, pady=5)
rb5.grid(column=0, row=5, padx=5, pady=5)


frame2 = tkinter.Frame(window, width=500, height=300, relief="sunken")
frame2.grid(column=1, row=0, padx=10, pady=10, sticky=tkinter.W)
label_seleccionado = tkinter.Label(frame2, text=f"Opcion seleccionada:  ")
label_seleccionado.grid(column=0, row=0, padx=10, pady=10)
labe2 = tkinter.Label(frame2, text="Boton reset seleccion")
labe2.grid(column=0, row=1, padx=10, pady=10)
botonReset = tkinter.Button(frame2, text="Reset", command=resetSeleccion)
botonReset.grid(column=0, row=2, padx=10, pady=10)


window.mainloop()
sys.exit(0)
