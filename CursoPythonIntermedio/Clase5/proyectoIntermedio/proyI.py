##Gesturas de Posicion

#Place()
import tkinter
from tkinter import *

v=tkinter.Tk()
v.title("Inicio de sesión")
v.geometry("500x600")
img = tkinter.PhotoImage(file='iconChat.png')
v.tk.call('wm', 'iconphoto', v._w, img)
v.resizable(False,False)

#v=Tk()

label1=Label(v,text="Usuario")
label1.place(x=10,y=10)
e1=Entry(v,bd=8)
e1.place(x=170,y=180)

label2=Label(v,text="Contraseña")
label2.place(x=10,y=50)
e2=Entry(v,bd=8)
e2.place(x=170,y=260)



def inicioSesion():
	e3.delete(0,len(e3.get()))
	e3.insert(0,str((int(e1.get())+int(e2.get()))/2))


boton=Button(v,text="Iniciar sesión",command=inicioSesion)
boton.place(x=210,y=450)



v.mainloop()
