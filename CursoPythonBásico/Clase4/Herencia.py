###
#

class Terrestre:
	def moverse(self):
		return("soy un "+self.__class__.__name__+"y camino en la tierra")
class Animal:
	def __init__(self,patas,nombre,peso):
	#Atributos
		self.patas=patas
		self.nombre=nombre
		self.energia=0
		self.peso=peso

	def comer(self):
		self.energia +=1

	def hablar(self):
		print("Grrrrr!")

#Un perro es un animal y es terrestre


class Perro(Animal): #Dentro de la clase, va de donde vamos a heredar()
	def __init__(self,nombre,peso):
		super().__init__(4,nombre,peso) 
#Se va a mandar a llamar cuando se mande a imprimir el objeto por medio de print "como se tiene que representar"
	def __str__(self):
		return str("Soy un objeto perro :3 ")
	def hablar(self):
		print("Guauuuu! Guauuuuu!")

Lucho=Perro("Lucho",30)
Pancho=Perro("Pancho",20)

Lucho.hablar()
Lucho.comer()


