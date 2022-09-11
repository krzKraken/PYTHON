# PyGtk
# PyQt5
# wxPython
# tKinter - tkinter Designer

# instalar en mac -> en windows ya esta instalado
# brew search tkinter
# brew search tk
# brew isntall python-tk@3.9

# tcl/tk ->
# tcl es un lenguaje de programacion
# tk -> toolKit en lenguaje de tcl

from pprint import pprint
import tkinter
from turtle import left

# contenedores -> frames o ventanas
window = tkinter.Tk()
# print(type(window))
# pprint(dir(window))
# loop

label1 = tkinter.Label(window, text="Label1", bg="red", fg="white")
label1.pack(ipadx=100, ipady=20, fill="x")
label2 = tkinter.Label(window, text="Label2", bg="blue", fg="white")
label2.pack(ipadx=100, ipady=20, fill="x")
label3 = tkinter.Label(window, text="Label3", bg="black", fg="white")
label3.pack(ipadx=100, ipady=20, fill="x")
label4 = tkinter.Label(window, text="Label4",  bg="green", fg="white")
label4.pack(ipadx=100, ipady=20, fill="y", side="left")
label5 = tkinter.Label(window, text="Label5", bg="black", fg="white")
label5.pack(ipadx=100, ipady=20, fill="both", side="left")
label6 = tkinter.Label(window, text="Label6",  bg="green", fg="white")
label6.pack(ipadx=100, ipady=20, fill="y", side="right")
# Geometrias ::::  Grip - Place


window.mainloop()
