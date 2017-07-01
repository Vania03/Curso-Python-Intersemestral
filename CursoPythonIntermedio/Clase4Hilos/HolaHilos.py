from threading import Thread
import threading
import time

def loop(nombre,n):
	for i in range(1,n):
		time.sleep(1)#Con esto hacemos que espere un segundo
		print(nombre,": ",i)
#arg argumentos que 
#para funcion los parametrso son: targets y args
while True:
	t1=Thread(target=loop,args=("hilo a",16))
	t1.start()
	t2=Thread(target=loop,args=("hilo b",11))
	t2.start()
#con esta linea= threading.active_count, nos regresa un entero que indica 
#el numero de hilos que esta corriendo o vivos en ese momento
	print("En este momento hay: ",threading.active_count(),"hilos corriendo")
	print(threading.enumerate())
#Con esto: threading.currentThread().name, sabemos el nombre del hilo
	print("El hilo actual es: ",threading.currentThread().name)
	print(threading.enumerate())	
#Join sirve para sincronizar las tareas
	t1.join()
	t2.join()

	repetir=input("Si quieres repetir, presiona S, si no presiona N\n")
	if repetir=="n" or repetir=="N":
		break


