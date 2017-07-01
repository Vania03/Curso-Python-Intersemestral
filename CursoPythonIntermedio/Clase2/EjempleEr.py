#Ejemp reg
import re
"""celular=input("Dame tu numero celular: ")

#vamos a hacer la expresionregular
patron="55[0-9]{8}"#empiezan con 55, datos validos del 0 al 9 y solo 8 caracteres

valido=re.match(patron,celular)
if valido:
	print("Telefono valido de la CDMX")
else:
	print("Favor de verificar")"""




"""entero=input("Dame un entero: ")

#patron="\d"= rango numericos y el mas porque no se cuantos numeros entonces de 1 a muchos

patron="\d+[^\.]"#\=deja de ser una metacaracter, lo esta escapando
valido=re.match(patron, entero)
if valido:
	print("Si es un entero")
	entero=int(entero)#vamos a castear aqui  los enteros hasta que estemso segiros que es un entero
else:
	print("No te creo")"""


correo='allanstone19@gmail.com'
 
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$',correo):
	print ("Correo correcto")
else:
	print ("Correo incorrecto")





