lista=[1,2,3,4,5]

try: 
	print("Busqueda: ", 2 in lista)
except IndexError:
	print("Este elemento no se encuentra dentro de la lista")
else:
	print("Todo esta bien no se levanto ninguna excepcion ")
