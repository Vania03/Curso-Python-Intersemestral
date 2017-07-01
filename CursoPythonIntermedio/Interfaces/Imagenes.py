##################
# Imagenes tkinter
##################

from tkinter import *

ventana=Tk()
logo=PhotoImage(file="FCA.png")
lbl1=Label(ventana,image=logo).pack(side="right")
texto="""Para utilizar imagenes con python,se debe utilizar los formatos PNG o GIF,
o utlizar el modulo PIL para otros formatos.
"""
lbl2=Label(ventana,justify=LEFT,padx=10,text=texto).pack(side="left")
ventana.mainloop()
