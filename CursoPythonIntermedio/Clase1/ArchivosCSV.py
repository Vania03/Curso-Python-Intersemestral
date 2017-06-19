###
#Archivos CSV

import csv

#manejador de contextos
with open("SampleCSVFile_2kb.csv","r") as f:
	reader=csv.reader(f)
	for linea in reader:
		print(linea)

f=open("SampleCSVFile_2kb.csv","r")
reader= csv.reader(f)

filas=0
for linea in reader:
	if filas==0:
		header=linea
	else:
		columnas=0
		for columna in linea:
			print("Fila: %d, Columna: %d, Contenido:%s"%(filas,columnas,dato))
	filas+=1