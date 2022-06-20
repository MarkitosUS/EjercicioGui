import tkinter
from tkinter import *
from turtle import reset

window = Tk()
opcion = IntVar()
window.geometry("300x300")
window.title("RadioButton")

def reset():
    opcion.set(None)

#Etiquietas

radio1 = Radiobutton(window, text="Opcion 1", value="1", variable = opcion)
radio1.place(x=10, y=40)

radio2 = Radiobutton(window, text="Opcion 2", value="2", variable = opcion)
radio2.place(x=10, y=70)

radio3 = Radiobutton(window, text="Opcion 3", value="3", variable = opcion)
radio3.place(x=10, y=100)

radio4 = Radiobutton(window, text="Opcion 4", value="4", variable = opcion)
radio4.place(x=10, y=130)

botonReset = Button(window, text="Resetear", command = reset)
botonReset.place(x=40, y=160)

window.mainloop()
