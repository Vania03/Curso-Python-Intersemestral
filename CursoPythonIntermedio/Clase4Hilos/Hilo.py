import threading
import time
x=0
#Esto es una herencia lo que va entre parentesis, entones la suma va a hereder lo de la resta
class Resta(threading.Thread):
	#Dentro del metodo run se va a realizar todo lo que me le metamos al hilo
	def run(self):
		#Variable local, solamente vive dentro de la funcion o metodo
		#Variable global,vive en todo el codigo
		global x #me va a permitir utlizar esa x dentro del metodo
		while x>0:
			x=x-1
			print("-: ",x)
			time.sleep(.5)

class Suma(threading.Thread):
	def run(self):#self: para decirle que es un metodo
		global x
		while x<50:
			x=x+3 #x+=3
			print("+: ",x)
			time.sleep(.5)
#Run manda a 
s= Suma()
r= Resta()

s.start()
r.start()

#Hay que sincronizar, para eso el metodo Join nos ayuda a hacer que un hilo espere a que otro termine
s.join()
r.join()