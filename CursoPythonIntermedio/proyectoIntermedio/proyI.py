#*-*coding:utf-8*-*
#Place()
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

import sqlite3
#########################BASE DE DATOS CRUD############################	
def insert(db, row):
    db.execute('insert into chat (usuario, contra) values (?, ?)', (row['usuario'], row['contra']))
    db.commit()

def retrieve(db, usuario):
    cursor = db.execute('select * from chat where usuario = ?', (usuario,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update chat set contra = ? where usuario = ?', (row['contra'], row['usuario']))
    db.commit()

def delete(db, usuario):
    db.execute('delete from chat where usuario = ?', (usuario,))
    db.commit()

def disp_rows(db):
	datos=[]
	contras=[]
	cursor = db.execute('select * from chat order by usuario')
	for row in cursor:
		info='{}'.format(row['usuario'])
		passwd='{}'.format(row['contra'])
		datos.append(info)
		contras.append(passwd)
		#print(datos)
		#print(contras)
	return datos
def rPass(db):
	contras=[]
	cursor = db.execute('select * from chat order by usuario')
	for row in cursor:
		passwd='{}'.format(row['contra'])
		contras.append(passwd)
		#print(contras)
	return contras


#####################CONEXIÓN A LA BASE################################
db = sqlite3.connect('chat.db')
db.row_factory = sqlite3.Row
try:
	print('Se ha creado la base de datos del chat')
	#db.execute('drop table if exists chat')
	#disp_rows(db)
	db.execute('create table chat ( usuario text, contra int )')
except sqlite3.OperationalError:
	print('La base ya existe')
#########################################################################
def hablar():
	chat=tkinter.Toplevel(v)
	chat.title("Chat del hogar")
	chat.geometry("500x600")
	chat.resizable(False,False)
	lUser=Label(chat,text="Ingresa la IP: ")
	lUser.place(x=80,y=230)
	e1=Entry(chat,borderwidth=3)
	e1.place(x=170,y=230)
	boton=Button(chat,text="Comenzar a hablar",relief=RAISED,width=10,height=5,command=hablar)
	boton.place(x=200,y=400)

def entra():
	chat=tkinter.Toplevel(v)
	chat.title("Chat del hogar")
	chat.geometry("500x600")
	chat.resizable(False,False)
	lUser=Label(chat,text="Ingresa la IP: ")
	lUser.place(x=80,y=230)
	e1=Entry(chat,borderwidth=3)
	e1.place(x=170,y=230)
	boton=Button(chat,text="Comenzar a hablar",relief=RAISED,width=10,height=5,command=hablar)
	boton.place(x=200,y=400)


	
def administrador():
	laux=[]
	admin = tkinter.Toplevel(v)
	admin.title("Administrador")
	admin.geometry("500x600")
	admin.resizable(False,False)
	#print(disp_rows(db))
	lb = Listbox(admin,selectmode=SINGLE,width=62,selectforeground="#ffffff",selectbackground="#88ADE7",selectborderwidth=3)
	lb.place(x=0,y=0)
	for item in disp_rows(db):
		lb.insert(END, item)
		laux.append(disp_rows(db).index(item))
	

	boton=Button(admin,text="Actualizar",relief=RAISED,width=10,height=5,command=inicioSesion)
	boton.place(x=200,y=300)
	boton2=Button(admin,text="Borrar",relief=RAISED,width=10,height=5,command=lambda: delete(db,lb.get(ACTIVE)))
	boton2.place(x=200,y=400)





def inicioSesion():
	#e3.delete(0,len(e3.get()))
	#e3.insert(0,str((int(e1.get())+int(e2.get()))/2))
	if e1.get()=='':
		messagebox.showinfo("Error" , "Error, falta el usuario")
	elif e2.get()=='':
		messagebox.showinfo("Error" , "Error, falta la contraseña")
	elif e1.get()=='admin' and e2.get()=='admin':
		administrador()
	else:
		if e1.get() in disp_rows(db) and e2.get() in rPass(db):
			entra()
		else:
			messagebox.showinfo("Error" , "Usuario inexistente o datos erronéos")






	print(e1.get())
	print(e2.get())
def registrarse(user,contrasenia):
	print(user,contrasenia)
	insert(db, dict(usuario = user, contra = contrasenia))

	
def v_registrarse():

	registro = tkinter.Toplevel(v)
	registro.title("Regístrate gratis")
	registro.geometry("500x600")
	registro.resizable(False,False)
	lUser=Label(registro,text="Usuario: ")
	lUser.place(x=80,y=230)
	lPass=Label(registro,text="Contraseña: ")
	lPass.place(x=80,y=310)
	e1=Entry(registro,borderwidth=3)
	e1.place(x=170,y=230)
	#Para ingresar la pass
	e2=Entry(registro,borderwidth=3,show="*")
	e2.place(x=170,y=310)

	#Registrarse
	boton=Button(registro,text="Registrarse",relief=RAISED,width=10,height=5,command=lambda: insert(db, dict(usuario = e1.get(), contra = e2.get())))
	boton.place(x=200,y=400)
	print(boton)
	#Cancelar
	boton2 = Button(registro,text="Cancelar",command=registro.destroy)
	boton2.place(x=200,y=500)	


	
	#v.iconify()

v=tkinter.Tk()
v.title("Inicio de sesión")
v.geometry("500x600")
#img = tkinter.PhotoImage(file='iconChat.png')
#v.tk.call('wm', 'iconphoto', v._w, img)
v.resizable(False,False)

#v=Tk()
#Usuario
label1=Label(v,text="Usuario")
label1.place(x=80,y=230)
#Contraseña
label2=Label(v,text="Contraseña")
label2.place(x=80,y=310)
#PROTECO PYTHON
##################################
label3=Label(v,text="PROTECO,curso: Python Intermedio.")
label3.place(x=30,y=540)
#Datos
label4=Label(v,text="Hecho por: Vania Martínez Troncoso.")
label4.place(x=30,y=570)

imagen = Image.open("rsz_2blogimage_chat_1.jpg")
princess = ImageTk.PhotoImage(imagen)

label5 = Label(image=princess)
label5.imagen = princess # keep a reference!
label5.place(x=0,y=0)

#Para ingresar el usuario
e1=Entry(v,borderwidth=3)
e1.place(x=170,y=230)

#Para ingresar la pass
e2=Entry(v,borderwidth=3,show="*")
e2.place(x=170,y=310)


boton=Button(v,text="Iniciar sesión",relief=RAISED,width=10,height=5,command=inicioSesion)
boton.place(x=200,y=400)

boton2 = Button(v,text="Regístrate",command=v_registrarse)
boton2.place(x=200,y=500)
v.mainloop()
