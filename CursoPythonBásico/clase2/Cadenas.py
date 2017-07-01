# -*- coding: utf-8 -*-
###
# Cadenas
###


cadena="hola"
cadena2="mundo"
cadenaLarga="""Esta es una
cadena
con
saltos
de
linea"""
cadenaVacia=""
cadenacruda=r"hola\n\r\t"

#print(cadena)
#cadena(cadenaCruda)
print("tipo de dato: ",type(cadena))
print("Indexación: ",cadena[0])
#Se pueden usar indices negativos y regresan la posicion del chr
print("Indexación: ",cadena[-2])
print("Tamaño: ",len(cadena))
print("Concatenación: ",cadena+cadena2)
print("Repetición: ",cadena*3)
#Asignación
#cadena[0]="H"
#Pueden ser Opcionales [inicio:fin+1]
print("Slicing: ",cadena[1:3])