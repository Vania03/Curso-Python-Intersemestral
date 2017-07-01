#-*-coding:utf-8-*-
#Er2
#1.-Importar modulo
import re
#2.-Buscar en texto
texto= "En este texto se encuentra la palabra mágica"

#re.search(regax,texto)regresa un booleano
#Search, nos regresa las posiciones

encontrado=re.search("mágica",texto)
print("Encontró la palabra?: ",encontrado)
print(encontrado.start())#donde empieza
print(encontrado.end())#donde acaba la palabra
print(encontrado.span())#De donde a donde va la palabra
print(texto[38:44])#Imprimri de donde a donde

#Match,a traves de Expresiones Regulares para saber si existe o no, es decir un booleano
texto="Hola mundo"
encontrado=re.match("Ho{0,1}la",texto)
if encontrado:
	print("Hizo coincidencia")
else:
	print("No hay coincidencia")
econtrado=re.match

#SPLIT
texto="Vamos a dividir esta cadena"
encontrado=re.split(" ", texto)#cuando encontro el espacio dividio la cadena, y nos regresa una lista de la cadena
print(encontrado)#Regreso una lista sin el caracter

print(" ".join(encontrado))#para pasar de una lista a una cadena, utilizamos la expresion join

# \d -> [0-9]
# \D -> [^0-9]	

#Metacaracter .
#. = Cuaqkuier car ater una sola vez
texto="ola ala ula pla alo ilo"
patrones=[".la",".lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
buscar(patrones,texto)


#Metacaracter *
#* = Puede estar o no estar, y si esta puede estar muchas veces, 0 o muchas
texto="hla hola hoola hooola hooooooooola hulo huuuulo"
patrones=["h*la","h*lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
buscar(patrones,texto)


#Metacaracter +
#+ = A fuerzas tiene que estar una sola vez o muchas, 1 o  muchas
texto="hla hola hoola hooola hooooooooola hulo huuuulo"
patrones=["h+la","h+lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
buscar(patrones,texto)

#puede estar 0 o una vez o ni una vez

#Metacaracter ?
#? = 0 or 1
texto="hla hola hoola hooola hooooooooola hulo huuuulo"
patrones=["h?la","h?lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))
buscar(patrones,texto)