from functools import reduce

class Vector:
	def __init__(self,elementos):
		self.elementos=elementos           
		self.dimension=len(elementos)   #Voy a tener dos atributos

	def __str__(self):
		"""Se manda a llamar cuando lo usemos como una cadena"""
		return "Vector: "+str(self.elementos)+" Dimension: "+str(self.dimension)

	def __getitem__(self,index):
	#Indexear el elemento como una lista #Vector [0]
		return self.elementos[index]

	def __setitem__(self,index,valor):
		"""Asignar el valor como si fuera una lista""" #Vector[0]=1
		self.elementos[index]=valor

	def __add__(self,otro):
		return Vector([self[i]+otro[i] for i in range(self.dimension)])

	def __sub__(self,otro):
		return Vector([self[i]-otro[i] for i in range(self.dimension)])

	def norma(self):
		acum=0
		for n in range(self.dimension):
			acum+=(self[n])**2
		return acum**(1/2)

	def normaMejorada(self):
		return reduce(lambda a,b: a+b,list(map(lambda x:x**2, self.elementos)))**(1/2)



if __name__ == '__main__':
	v1=Vector([1,2,3])
	v2=Vector([2,4,6])


#Prueba para __getitem__
	print("v1[0]=",v1[0])#1

#Prueba para __setitem__
#v1[0]=0
	#print

	v3=v1=v2

	print("v1 ",v1)
	print("v2 ",v2)
	print("v3 ",v3)
	print(v1.norma())
	print(v1.normaMejorada())


