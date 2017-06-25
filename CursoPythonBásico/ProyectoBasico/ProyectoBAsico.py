#-*-coding:utf-8-*-
import os
from calcComplejos import Complejos
from calcPoli import calcPol
from Gato import Gatuno
print("*********************Proyecto del Curso Basico de Python****************")

while True:
	try:
		print("\n\t\t1.-Calculadora de Complejos")
		print("\n\t\t2.-Calculadora de Polinomios")
		print("\n\t\t3.-Juego del Gato")


		opcionMenu=int(input("Opción: "))

		if opcionMenu==1:
			os.system("clear")
			Complejos()
		elif opcionMenu==2:
			os.system("clear")
			calcPol()
		elif opcionMenu==3:
			os.system("clear")
			Gatuno()
		elif opcionMenu==0:
			print("****************** Adios :) *********************")
			break
		else:
			os.system("clear")
			print("\n\n\tOpción no válida, intenta de nuevo!")
	except ValueError():
		print("Esto no es un numero, intenta de nuevo")


		