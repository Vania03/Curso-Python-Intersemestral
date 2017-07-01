#-*-coding:utf-8-*-
#E

import re

"""def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))

patrones=["ho{0,1}la","ho{1,2}la"]
texto="hla hola hoola hoola hooooola"""

"""def buscar(patrones, texto): 
	for patron in patrones:
		print(re.findall(patron,texto)) 
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
texto = "hala hela hila hola hula" 
buscar(patrones, texto)"""

def buscar(patrones, texto): 
	for patron in patrones:
		print( re.findall(patron, texto) )
patrones = ['h[a‐z]la', 'h[0‐9]la', '[A‐z]{4}', '[A‐Z][A‐z0‐9]{3}'] #{4}cualquier caracter de 4 letras
texto = "hola h0la Hola mola m0la M0la Abcd acde"
buscar(patrones, texto)