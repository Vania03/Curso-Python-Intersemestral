###
#Polimorfismo

class Animal:

	def __init__(self,nombre):
		self.nombre=nombre
#Metodo Abstracto, porque no esta definido
	def hablar (slef):
		raise NotImplementedError("Debes implementar antes!")

class Perro(Animal):
	def hablar(self):
		return("Guauuuu!!!")

class Gato(Animal):
	def hablar(self):
		return("Miauuuuu!!!")

animales=[Gato("Gatosan"),	
		Perro("Max"),
		Gato("Bigotes")]

for animal in animales:
	print(animal.nombre+" dice "+animal.hablar())


a=Animal("Fantasma")