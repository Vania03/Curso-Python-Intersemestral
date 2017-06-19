class Animal():
	def __init__(self,especie,nombre):
		self.especie=especie
		self.nombre=nombre     #Atributo publico

class Animal():
	def __init__(self,especie,nombre):
		self.especie=especie
		self.__nombre=nombre #Atributo privado
	def getNombre(self):
		return self.__nombre

	def setNombre(self,nombre):
		self.__nombre=nombre

	@property
	def __nombre(slef):
		print("Llamando a el Getter")
		return self._nombre

	@__nombre.setter
	def __nombre(self,nombre):
		print("Llamando a el Setter")
		self._nombre=nombre


rafael=Animal("toruga", "Rafael")
#print("El animal tiene nombre ", rafael.nombre)
print("El animal es de especie: ", rafael.especie)
rafael.especie="gatito"
print("El animal es de especie ", rafael.especie)
#print("El animal tiene nombre: ", rafael.getNombre)
#rafael.especie="gatito"
print("El animal tiene nombre: ", rafael._nombre)