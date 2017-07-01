###
#Botones
###
from tkinter import *
from tkinter import messagebox
v=Tk()

def alertaCallback():
	msg=messagebox.showinfo("Alerta","Este es un mensaje de alerta")

def textCallback():
	v=Toplevel()
	text=Text(v)

	#Esta es insercion de datos
	text.insert(INSERT,"Hola desde...")
	text.insert(END,"Aqui :V ")
	text.pack()

	text.tag_add("amarillo","1.0","1.4")
	text.tag_add("morado","1.8","1.13")

	text.tag_config("amarillo",background="yellow",foreground="purple")
	text.tag_config("morado",background="purple",foreground="white")

def msgCallback():
	v=Toplevel()
	#Si fuera una IntVar(), diferentes a String y a Int respectivamente
	var=StringVar()
	label=Message(v,textvariable=var,relief=RAISED)
	#Modifica a la variable var
	var.set("Hola, como estan?")
	label.pack()

b1=Button(v,text="Alerta",command=alertaCallback)
b1.place(x=50,y=50)

b2=Button(v,text="Texto",command=textCallback)
b2.place(x=50,y=100)

b3=Button(v,text="Mensaje",command=msgCallback)
b3.place(x=50,y=150)

v.mainloop()
