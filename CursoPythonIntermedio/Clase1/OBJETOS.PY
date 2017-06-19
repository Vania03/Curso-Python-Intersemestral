class Animal:
	pass #Acordarse de programar esto despues

class Volador:
	pass

class Ave(Animal,Volador):
	def __init__(self,plumas):
		#Inicializacion atributos
		self.plumas=plumas

	#ya estan los parametros, vamos a definir los metodos de clase
	@classmethod
	#la clase se esta pasando como prametro.
	def volar(par1):
		print(par1)

	def hablar(self):
		return "Pio"

		#Objeto de la clase ave

pollito=Ave("muchas plumas")

#Metodo de clase, asi se invoca un metodo de clase, el objeto se pasa como parametro
pollito.volar()
Ave.volar()

#Mesotod de clase, o instancia
print(pollito.hablar())


