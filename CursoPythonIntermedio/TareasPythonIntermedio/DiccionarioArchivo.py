###
import sys
correo={}
contactos={}
conta=0
with open(input("Ingrese el nombre del archivo: ")) as d:
	lineas=d.readlines()
for linea in lineas:
	nueva=linea.split()
	contactos[nueva[conta]]=nueva[conta+1]
	correo[nueva[conta]]=nueva[conta+2]
print(contactos)
print(correo)
for persona in contactos.keys():
	print("El numero de ",persona,"es: ",contactos[persona]," y su email es: ",correo[persona])

