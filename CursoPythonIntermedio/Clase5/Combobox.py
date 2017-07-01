#####
#Comb Box
#####

from tkinter import *
#Extras para Tkinter
from tkinter import ttk
ventana=Tk()

combo=ttk.Combobox(ventana)
combo.pack()
combo["values"]=("Mexico","Venezuela","Nicaragua","Ecuador","Argentina")

ventana.mainloop()
