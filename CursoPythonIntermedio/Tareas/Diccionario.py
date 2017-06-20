###
import sys
contactos={}
conta=0
with open(input("Ingrese el nombre del archivo: ")) as d:
	lineas=d.readlines()
for linea in lineas:
	nueva=linea.split()
	contactos[nueva[conta]]=nueva[conta+1]
print(contactos)
for persona in contactos.keys():
	print("El numero de ",persona,"es: ",contactos[persona])