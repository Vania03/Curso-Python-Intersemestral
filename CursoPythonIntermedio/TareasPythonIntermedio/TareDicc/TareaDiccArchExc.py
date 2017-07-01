###
import sys
import re
correo={}
contactos={}
conta=0
patronCel="55[0-9]{8}"
patronCorreo="^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$"
numerosErroneos=[]
correoErroneos=[]
with open(input("Ingrese el nombre del archivo: ")) as d:
	lineas=d.readlines()
for linea in lineas:
	nueva=linea.split()
	contactos[nueva[conta]]=nueva[conta+1]
	
	validoCel=re.match(patronCel,contactos[nueva[conta]])
	if validoCel:
		print("Telefono valido de la CDMX")
	else:
		numerosErroneos.append(nueva[conta+1])
		#print(numerosErroneos)
		print("Favor de verificar")
	correo[nueva[conta]]=nueva[conta+2]
	validoCorreo=re.match(patronCorreo,correo[nueva[conta]])
	if validoCorreo:
		print("Correo valido")
	else:
		correoErroneos.append(nueva[conta+2])
		#print(correoErroneos)
		print("Correo invalido!, favor de verificar correo")

print(contactos)
print(correo)
for persona in contactos.keys():
	print("El numero de ",persona,"es: ",contactos[persona], " y su correo es: ", correo[persona])

for numeros in numerosErroneos:
	print("Verificar el numero: ",numeros," ya que es un telefono invalido")

for correos in correoErroneos:
	print("Favor de verificar su direccion de correo electronica: ",correos)

for correos in correo:
	print("El correo de : ",correos,"es valido")	