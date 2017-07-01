import threading
#Definimos la funcion que realizara el hilo
def saluda(nombre):
	print("Hola", nombre)
#Creamos dos onjetos de tipo Thread
hilo= threading.Thread(target=saluda,args=("Jorge",))
hilo2=threading.Thread(target=saluda,args=("Alan",))
hilo3=threading.Thread(target=saluda,args=("Vania",))
hilo4=threading.Thread(target=saluda,args=("Mauricio",))
hilo5=threading.Thread(target=saluda,args=("Gaby",))
hilo6=threading.Thread(target=saluda,args=("Julio",))
hilo7=threading.Thread(target=saluda,args=("Marla",))
hilo8=threading.Thread(target=saluda,args=("Elsa",))
#Inicializamos los hilos
hilo.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()
hilo8.start()
