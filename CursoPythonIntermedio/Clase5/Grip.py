##Gesturas de Posicion

#Grid()
from tkinter import *

v=Tk()

"""i=0
for x in range (6):
	for y in range (6):
		i+=1
		Button(v,text=str(i),borderwidth=1).grid(row=x,column=y)"""

ButtonI=Button(v,text="Estoy en la izquierda").grid(row=0,column=0)
ButtonD=Button(v,text="Estoy en la derecha").grid(row=0,column=1)

		
v.mainloop()

