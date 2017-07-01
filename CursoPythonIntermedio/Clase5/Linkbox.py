#####
#Link Box
#####

from tkinter import *
import webbrowser
ventana=Tk()

def linkCallback():
	#Aqui abrimos un navegador para acceder a la pag dicha
	#(r"blabla./)es una cadena cruda y omite los caracteres
	webbrowser.open_new(r"http://www.google.com")
	#fg cambia el color del texto
link=Button(ventana,text="Google",fg="green",cursor="hand2",command=linkCallback)
link.pack()

ventana.mainloop()
