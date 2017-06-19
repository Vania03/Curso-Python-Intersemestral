


diccionario={1:"Opcion 1", 2:"Opcion 2", 3:"Opcion 3"}
#list casteamos a una lista
#keys nos lleva a las llaves
lista=list(diccionario.keys())
#pero esta en desorden, entonces hay que ordenarlos
lista.sort()
print(lista)

while True:
	for llave in lista:
		print("\t%s. %s"%(llave,diccionario[llave]))
	seleccion=int(input("Selecciona una opcion: "))
	if seleccion in lista:
		print("Seleccionaste la: ", diccionario[seleccion])


	#else:
		#print("Opcion Invalida")


	#else:
		#print("Adios")
		#break
	elif seleccion == 0:
		print("Adios")
		break
	else:
		print("Opcion invalida")


