#-*-coding:utf-8-*-
print("*********************Proyecto del Curso Basico de Python****************")

while True:
	try:
		print("\n\t\t1.-Calculadora de Complejos")
		print("\n\t\t2.-Calculadora de Polinomios")
		print("\n\t\t3.-Juego del Gato")


		opcionMenu=int(input("Opción: "))

		if opcionMenu==1:
			os.system("clear")
			pass
		elif opcionMenu==2:
			os.system("clear")
			pass
		elif opcionMenu==3:
			os.system("clear")
			pass
		elif opcionMenu==0:
			print("****************** Adios :) *********************")
			break
		else:
			os.system("clear")
			print("\n\n\tOpción no válida, intenta de nuevo!")
	except ValueError():
		print("Esto no es un numero, intenta de nuevo")


		