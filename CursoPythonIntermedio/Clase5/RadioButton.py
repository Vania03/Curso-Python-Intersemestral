#####
#RadioButton	
#####

from tkinter import *

v=Tk()
var=StringVar()
def seleccion():
	#objeto.get()nos regrresa el valor del objeto asignado por value
	select="Tu seleccion fue: "+(var.get())
	#.config modifica al objeto, en este caso modificamos al texto
	label.config(text=select)
#INstancia:
#objeto:(ventana,argumento,argumento)
#argumento son modificadores del objeto
#Command corresponde a la accion que realiza el objeto

r1=Radiobutton(v,text="Opcion 1",variable=var,value="1",command=seleccion).pack()
r2=Radiobutton(v,text="Opcion 2",variable=var,value="2",command=seleccion).pack()
r3=Radiobutton(v,text="Opcion 3",variable=var,value="3",command=seleccion).pack()

label=Label(v)
label.pack()

v.mainloop()
