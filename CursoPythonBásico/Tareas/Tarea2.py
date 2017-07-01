#-*-coding:utf-8-*-
import os 
import random
#Funciones
#1
def uno():
	for i in range(1500,2701):
		if i%7==0 and i%5==0:
			print("El numero ",i,"es divisible entre 7 y multiplo de 5")
def dos(grado):
	eleccion=input("Si quieres convertir de Grados Celsius a grados Fahrenheit, presiona F\nSi quieres convertir de grados Fahrenheit a grados Celsius, presiona C\t\nElección: ")
	if eleccion=="F" or eleccion=="f":
		Fahrenheit=(9/5*grado)+32
		return Fahrenheit
	elif eleccion=="C" or eleccion=="c":
		Celsius=(grado-32)*(5/9)
		return Celsius
	else:
		print("Opción incorrecta, intenta de nuevo.")
def tres():
	numeroadivinador=random.randrange(1,10)
#print(numeroadivinador)
	while True:
		numeroInsertado=int(input("Adivina un número entro el 1 y el 9: \nNúmero:"))
		if numeroInsertado==numeroadivinador:
			print("Tu número: ",numeroInsertado," es igual al número que tenía en mente: ",numeroadivinador,"\t GANASTE!!!!")
			break
		else:
			print("Tu numero: ", numeroInsertado," es diferente al numero que tenia en mente, INTENTA DE NUEVO :(")
def cuatro():
	p1=[1,2,3,8,9,8,3,2,1]

	for n in p1:
		if n%2==0:
			print(">"*n)
		else:
			print("* "*n)
	for n in p1 [0:5:-1]:
		if n%2==0:
			print(">"*n)
		else:
			print("* "*n)
def cinco():
	while True:
			palUsuario=input("Ingresa una frase o una s para salir: ")
			if palUsuario=="s" or palUsuario=="S":
				print("Regresa pronto :)")
				break
			else:
				print("Tu frase: ",palUsuario)
				palUsuario=list(palUsuario)
				inversa=palUsuario[::-1]
				print("Tu frase invertida: ",inversa)
def seis():
	print("Reconoceremos los impares y pares de tu lista")
	listaNumeros=[]
	pares=[]
	impares=[]
	while True:
		numero=int(input("Ingresa un numero a la lista o presiona 0 para terminar de ingresar: "))
		if numero==0:
			print("\n\nTu lista es: ",listaNumeros)
			break
		else:  
			listaNumeros.append(numero)
		print(listaNumeros)
	for elemento in listaNumeros:
		if elemento%2==0:
			pares.append(elemento)
			#print("Los numeros pares son: ",elemento)
		else: 
			impares.append(elemento)
			
			#print("Los numeros impares son: ",elemento)
	print("Hay: ",len(pares),"números pares en tu lista.")
	print("Hay: ",len(impares),"números impares en tu lista.")

def siete():
	datalist=[1452, 11.23, 1 + 2j, True, "w3resource", (0, -1), [5, 12], {"clase": 'V', 'section': 'A'} ]
	for elemento in datalist:
		print("Elemento: ",elemento," es de tipo: ",type(elemento))	

def ocho():
	a=-1
	while a<6:
		a=a+1
		if a==3:
			continue
		elif a==6:
			continue
		else: 
			print(a)	
	print("Se ha terminado... :s ")

def nueve(num):     #definicion
	if num<1:
		return 1         # Condicion de paro
	else:					#2*1*1
		return num*nueve(num-1)    #Llamando a la funcion 
def diez():
	vocales=["a","A","e","E","i","I","o","O","u","U"]
	res=""
	while True:
		fraseUsuario=input("Ingresa una frase o una s para salir: ")
		if fraseUsuario=="s" or fraseUsuario=="S":
			print("Regresa pronto :)")
			break
		else:
			print("Tu frase: ",fraseUsuario)
			fraseUsuario=list(fraseUsuario)
			for elemento in fraseUsuario:
				if elemento not in vocales:
					res += elemento
			print("Tu frase sin vocales es: ",res)	
def once(peso,estatura):
	IMC=peso/estatura**2
	if IMC<18.50:
		print("Te encuentras en: Infrapeso, come más!!")
		return IMC
	elif IMC>18.50 and IMC<25:
		print("Te encuentras en: Estado Normal ")
		return IMC
	elif IMC>25 and IMC<30:
		print("Tienes Sobre Peso, Haz ejercicio!!")
		return IMC
	elif IMC>30 and IMC<35:
		print("Tienes obesidad leve, Cuidate!! ")
		return IMC
	elif IMC>35 and IMC<40:
		print("Tienes obesidad media, bajale a las gorditas!!!")
		return IMC
	elif IMC>40:
		print("Tienes obesidad alta, estas muy cerca de un infarto!!, Ve al doctor!!!")
		return IMC



print("************************************ MENU DE RESOLUCION DE PROBLEMAS *******************************")
while True:
	print("\n\t\tSeleccione la opción que desee que el programa resuelva")
	print("\n\t\t1.-Calcular números divisibles entre 7 y multiplos de 5")
	print("\n\t\t2.-Conversión de grados Celsius a Fahrenheit y de grados Fahrenheit a Celsius")
	print("\n\t\t3.-Adivinador de números entre 1 y 9")
	print("\n\t\t4.-Ver la pirámide egipcia :v")
	print("\n\t\t5.-Juega con el invertidor de palabras")
	print("\n\t\t6.-Contador de números pares e impares de tus series númericas")
	print("\n\t\t7.-Reconocedor de tipos de datos")
	print("\n\t\t8.-Impresión de números")
	print("\n\t\t9.-Calculador de Factoriales")
	print("\n\t\t10.-Juega como se leen tus frases favoritas sin vocales")
	print("\n\t\t11.-Determine su IMC y descubra si encuentra saludable!")
	print("\n\t\t0.-Salir")

	opcionMenu=int(input("Opción: "))
	if opcionMenu==1:
		os.system("clear")
		uno()
	elif opcionMenu==2:
		os.system("clear")
		grados=float(input("Ingresa tus grados Celcius o Fahrenheit: "))
		grados=dos(grados)
		print("El resultado de tu eleccion es: ",grados)
	elif opcionMenu==3:
		os.system("clear")
		tres()
	elif opcionMenu==4:
		os.system("clear")
		cuatro()
	elif opcionMenu==5:
		os.system("clear")
		cinco()
	elif opcionMenu==6:
		os.system("clear")
		seis()
		pass
	elif opcionMenu==7:
		os.system("clear")
		siete()
	elif opcionMenu==8:
		os.system("clear")
		ocho()
	elif opcionMenu==9:
		os.system("clear")
		a=int(input("De qué número quiere saber su factorial? "))
		nueve(a)
		print("El factorial de su número seleccionado es: ",nueve(a))

	elif opcionMenu==10:
		os.system("clear")
		diez()
	elif opcionMenu==11:
		os.system("clear")
		peso=float(input("Ingresa tu peso: "))
		estatura=float(input("Ingresa tu estatura: "))
		IMC= once(peso,estatura)
		print("Tu IMC es: ",IMC)
	elif opcionMenu==0:
		print("****************** Hasta luego, regresa pronto!! :D *********************")
		break
	else:
		os.system("clear")

		print("\n\n\tOpción no válida, intenta de nuevo!")
		
	

	
