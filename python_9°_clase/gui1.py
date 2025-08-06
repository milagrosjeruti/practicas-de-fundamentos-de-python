from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

ventana = Tk()
ventana.title("Menu principal")
ventana.config(bg="Red")
ventana.geometry("520x480")
ventana.resizable(0,0)

botonCalc = Button(text="calculadora", command=abrirCalculadora)
botonCalc.place(x=50, y=50)
botonCalc.config(bg="yellow")
ventana.mainloop()
