###
#Primer Ejemplo POO
###

class Persona:
	#Atributos
	edad=21
	saludo="Hola amigos"
#Este es un metodo de la clase persona, se llama como a una funcion con la diferencia de SELF
	def saludar(self):
		print("%s Soy una persona"%self.saludo)

	def unaFuncion():
		print("Esto es una funcion de clase")

#Instancia o creacion de un objeto a partir de una  clase

jorge=Persona()

print(jorge.edad)
print(jorge.saludo)

jorge.saludar()

Persona.unaFuncion()

print(Persona.edad)
