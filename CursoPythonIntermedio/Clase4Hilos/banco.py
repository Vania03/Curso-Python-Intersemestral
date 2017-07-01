###
#Exclusion mutua
####

import threading #Importamos el modulo threading
import time

class cuenta: #Creamos la clase cuenta
	def __init__(self,saldo):
		self.saldo=saldo
		self.candado=threading.Lock() #Definimos un candado

	#Definimos el metodo retirar
	def retirar(self,cantidad):
		self.candado.acquire() #El metodo acquire nos permite bloquear al hilo
		if self.saldo>0:
			time.sleep(1)
			print("Se hizo un retiro! ")
			self.saldo=self.saldo-cantidad
			print("Su saldo acutual es: ",self.saldo)
		self.candado.release()#El metodo release nos permite liberar al hilo

#crear objeto de tipo cuenta
c=cuenta(300)

h=[]#Creamos una lista para meter los hilos
for i in range(100):
	#Para acceder al metodo de los objetos es: objeto.metodo
	h.append(threading.Thread(target=c.retirar,args=(20,)))
for hilito in h:
	hilito.start()#Inicializamos todos los hilos de la lista
