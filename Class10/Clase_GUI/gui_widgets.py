# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

from tabnanny import check
import tkinter
from tkinter import Frame, ttk


import sys
from pprint import pprint

window = tkinter.Tk()


window.columnconfigure(0, weight=3)
window.rowconfigure(0, weight=3)

# Label en frame(0,0)
frame00_labbel = ttk.Frame(window, width=300, height=300, relief="sunken")
frame00_labbel.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
label = ttk.Label(frame00_labbel, text="__WIDGET LABEL___")
label.grid(sticky=tkinter.W, padx=10, pady=10)
label = ttk.Label(frame00_labbel, text=" Widget Label...")
label.grid(sticky=tkinter.W, padx=10, pady=10)

# list Box en Frame(0,1)
frame01_listBox = ttk.Frame(window, width=300, height=300, relief="sunken")
frame01_listBox.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=10)
label = ttk.Label(frame01_listBox, text="WIDGET LIST BOX")
label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
lista = ["Windows", "macOS", "Linux", "MS DOS"]
# Transforma la lista en una lista leible por tkinter
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(frame01_listBox, listvariable=lista_items, height=0)
listbox.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

# RadioButton en Frame(0,2)
frame02_radio_button = ttk.Frame(window, width=300, height=300, relief="sunken")
frame02_radio_button.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=10)
label = ttk.Label(frame02_radio_button, text="WIDGET RADIO BUTTON")
label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
# variable donde se va crear el valor seleccionado -> value=0 indica que valor por defecto es ninguno o el valor que corresponda a => 0
seleccionado = tkinter.StringVar(value=0)

r1 = tkinter.Radiobutton(
    frame02_radio_button,
    text="Si",
    value="1",
    variable=seleccionado,
)
r2 = tkinter.Radiobutton(
    frame02_radio_button,
    text="No",
    value="2",
    variable=seleccionado,
)
r3 = tkinter.Radiobutton(
    frame02_radio_button,
    text="QUIZAS",
    value="3",
    variable=seleccionado,
)
r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)


# Widget Check
frame03_check_button = ttk.Frame(window, width=300, height=300, relief="ridge")
frame03_check_button.grid(column=2, row=2, sticky=tkinter.W, padx=10, pady=10)

label = ttk.Label(frame03_check_button, text="WIDGET CHECK BUTTON")
label.grid(column=0, row=0, padx=5, pady=5)
seleccionado_check = tkinter.StringVar()
# funcion que ejecuta cuando selecciona el checkbox
def mifuncion():
    print("Clicado")


checkbox = ttk.Checkbutton(
    frame03_check_button,
    text="Acepto las condiciones",
    variable=seleccionado_check,
    command=mifuncion,
)
checkbox.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)


# button en frame 33 con evento
frame33_event_button = ttk.Frame(window, width=300, height=300, relief="ridge")
frame33_event_button.grid(column=3, row=3, sticky=tkinter.W, padx=10, pady=10)
label = tkinter.Label(frame33_event_button, text="BOTON EVENTO")
label.grid(column=0, row=0, padx=10, pady=10)
boton = tkinter.Button(frame33_event_button, text="Boton Evento")
boton.grid(column=1, row=1, padx=10, pady=10)


def saludar(event):
    print("Evento click izquierdo")


def despedir(event):
    print("Evento clic derecho")


def dobleclic(event):
    print("doble clic  izquierdo")


def salir(event):
    print("Adios")
    window.quit()


boton.bind("<Button-1>", func=saludar)
boton.bind("<Double-1>", func=dobleclic)
boton.bind("<Button-2>", func=despedir)

boton_salir = tkinter.Button(frame33_event_button, text="Salir")
boton_salir.grid(column=1, row=2, padx=10, pady=10)
boton_salir.bind("<Button-1>", salir)

window.mainloop()
sys.exit(0)
