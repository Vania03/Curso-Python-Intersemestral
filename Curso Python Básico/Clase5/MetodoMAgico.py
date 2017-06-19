###
#Metodo Magico
##

#Metodos que se manden a llamar automaticamente
class Coordenada:
	def __init__(self,x,y):
		self.x=x
		self.y=y
#Se manda  llamar cuando se quieren sumar los objetos por medio del operador +
	def __add__(self,otro):
		return Coordenada(self.x+otro.x,self.y+otro.x)
	#Se pueden sobreescribir todos los operadores, por ejemplo:
		#__add__ (+)
		#__sub__ (-)
		#__mul__ (*)
		#__div__ (/)
		#__pow__ (**)
		#__mod__ (%)
#Cuando se quiera acceder al objeto por medio de print()
	def __str__(self):
		return "(%d,%d)"%(self.x,self.y)
#Se va a mandar la llamar cuando se quiera acceder al objeto como si fuera una lista, con []
	def __getitem__(self,indice):
		if indice ==0:
			return self.x
		else:
			return self.y

#Se va amandar a llamar cuando se requiere asignar el objeto como si fuera una lista

	def __setitem__(self,indice,valor):
		if indice==0:
			self.x=valor
		else:
			self.y=valor

	#Ejemplo

c1=Coordenada(2,3)
c2=Coordenada(4,7)

print(c1) #Manda a llamar a C1.__str__()
print(c1+c2)#Manda a llamar a c1.__add__(c2)
print(c1[0]) #Manda a llamar a c1.getitem__(0)

c2[0]=10 #Mandar a llamar c2.__stitem__(0,10)

print(c2)



