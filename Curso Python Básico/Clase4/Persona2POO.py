###
#Persona 2 POO
###

class Persona2:
	##Constructor
	#Permite asignar a los objetos atributos 
	def __init__(self):
		print("Se ha creado una persona, y se imprimio este mensaje")
	def saludar(self):
		print("Hola soy una persona")
	def comer(self):
		print("Estoy comiendo, no me molestes!")
	def estudiar (self):
		print("Estoy aprendiendo POO")

juan=Persona2()
vania=Persona2()
alan=Persona2()

juan.saludar()
vania.estudiar()
alan.comer()
