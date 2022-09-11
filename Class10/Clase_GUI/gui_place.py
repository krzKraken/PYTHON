# Posicionamiento con Place
from operator import ne
import tkinter
from tkinter import ttk

window = tkinter.Tk()

label1 = tkinter.Label(window, text="Posicionamiento absoluto",
                       bg="blue", fg="white")
label1.place(x=10, y=50)
label2 = tkinter.Label(window, text="Otro MAs",
                       bg="red", fg="white")
label2.place(x=5, y=20)


window.mainloop()
