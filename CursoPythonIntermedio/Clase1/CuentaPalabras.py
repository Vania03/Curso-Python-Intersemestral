#Cuenta Palabras

import sys

nombreArchiv=sys.argv[1]

f=open(nombreArchiv,"r")

totalP=0
totalC=0
#read nos regresa cadenas, y readlines, nos regresa lineas
for linea in f.readlines():
	#cadena.split()asi quitamos los saltos de linea, nos regresa una lista[]
	#cadena.strip() este me regresa una cadena " ", ya sin los carcateres especiales
	#Lo ue ya habia contado anteriormente mas lo contado de este lado
	totalP+=len(linea.split())
	#totalp=totalp+len(linea.split())

	for palabra in linea:
		totalC+=len(palabra.strip())
		

print("La cantidad de palabras es: ",totalP)
print("La cantidad de caracteres es: ",totalC)

f.seek(0)
totalS=0

cadenas=f.read()
print(str(cadenas.split()))
lista=cadenas.split()

for palabra in lista:
	totalS+=len(palabra)

print("La cantidad de palabras es: ",len(lista))
print("La cantidad de caracteres es: ",totalS)




