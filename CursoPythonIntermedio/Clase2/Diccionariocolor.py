colores={"rojo":"red","verde":"green","negro":"black"}

try:
	print(colores["rojo"])
except KeyError:
	print("No existe ese color")
else:
	print("Todo esta bien no se levanto ninguna excepcion ")
