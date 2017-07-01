def suma(a,b):
	return a+b

a , b = 15 , 20
try:
	print(suma(a,b))

except TypeError:
	print("El dato que estas metiendo no es numero")
else:
	print("Todo esta bien no se levanto ninguna excepcion ")


