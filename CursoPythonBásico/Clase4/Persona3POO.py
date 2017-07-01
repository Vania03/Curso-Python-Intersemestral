###
#Persona3 POO
###

class Persona3:
	#Definir atributos
	def __init__(self,nombre,apellido,edad,estatura,dinero):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.estatura=estatura
		self.dinero=dinero
		print("Hola soy ",self.nombre," ",self.apellido,"y tengo ",self.edad,"anios, y mido ",self.estatura)
		print("Tengo $ ",self.dinero,"pesos en mi cuenta")

		
	def comer(self,comida):
		print("Soy: ",self.nombre," y estoy comiendo ",comida, "que rico!")
	def informarSaldo(self):
		print("Soy: ",self.nombre,"y actualmente tengo $ ",self.dinero,"en mi cuenta")


	def prestarDinero(self,monto,destinatario):
		self.informarSaldo()
		destinatario.informarSaldo()

		self.dinero=self.dinero-monto #Aqui les restamos la cantidad que va a prestar
		destinatario.dinero=destinatario.dinero+monto #Aqui le sumamos la cantidad a quien le prestaremos

		self.informarSaldo()
		destinatario.informarSaldo()

	#Metodo de la clase
	def regalarDinero(donacion,donador,beneficiado):

		donador.informarSaldo()
		beneficiado.informarSaldo()

		donador.dinero=donador.dinero-donacion
		beneficiado.dinero=beneficiado.dinero+donacion
		donador.informarSaldo()
		beneficiado.informarSaldo()

#Creacion de objetos

paco=Persona3("Paco","Nomeacuerdo",20,1.70,1000)
vania=Persona3("Alan","Garrido",23,1.80,200)

paco.comer("Pizza")

vania.informarSaldo()

paco.prestarDinero(500,vania)
print("******************************************************")

Persona3.regalarDinero(200,vania,paco)




