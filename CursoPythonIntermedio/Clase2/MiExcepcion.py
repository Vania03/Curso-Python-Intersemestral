###
#Mi Excepcion
#
#Asi declaramos una excepcion propia
class MiExcepcion(Exception):
	pass

try:#Aqui voy a meter mi codigo que me puede lanzar una excepcion 
	x=1.7172
	if isinstance(x,float):
		#Raise, va a obligar a que ocurra una exepcion, en este caso nuestra excepcion
		#Mando a llamar a mi excepcion con raise
		raise MiExcepcion
##Levantamos nuesta propia excepcion
except MiExcepcion: #Aqui vamos a poner las excepciones que se van a lanzar
	print("No es un entero")