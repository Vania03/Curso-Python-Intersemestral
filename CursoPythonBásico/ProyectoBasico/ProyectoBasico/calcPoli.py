#-*-coding:utf-8-*-
####################################
##CALCULADORA DE POLINOMIOS##
####################################

from scipy import *
from sympy import *
import os

def suma(a,b):
	return a+b
def resta(a,b):
	return a-b
def multiplicacion (a,b):
	return a*b
def division(a,b):
	return a/b

def  Evaluar(a,c):
	 libres = {"x": c}
	 return eval(a, {}, libres)
def raiz(polinomio):
	raices=roots(polinomio)
	for x in raices:
		print("La raíz del polinomio es: ",x)

def derivar(poli):
	init_printing()
	x,y=symbols('x,y')
	dx=diff(poli,x)
	return dx

def integrar(poll):
	init_printing()
	x,y=symbols('x,y')
	dz=integrate(poll,x)
	return dz

os.system("clear")
	
def calcPol():
	print("""
		                   ______        _   _ 
                                  (_____ \      | | (_)
  ___  _   _  ____   _____   ____  _____) )___  | |  _ 
 /___)| | | ||  _ \ | ___ | / ___)|  ____// _ \ | | | |
|___ || |_| || |_| || ____|| |    | |    | |_| || | | |
(___/ |____/ |  __/ |_____)|_|    |_|     \___/  \_)|_|
             |_|                                       
		""")
	print("\n\n\t\t\t")
	print('\n\t\t La variable a utilizar para el polinomio es "x"' )
	print("\n\t\t Ejemplo de un polinomio : 3*x**3+2*x**2+x+1")
	print("3*x=>3x")
	print("3**2=>3^2")	
	while  True:
		try:

			print("""\n¿Qué operación deseas realizar?")
			1.Sumar
			2.Restar
			3.Multiplicar
			4.Dividir
			5.Evaluar polinomio
			6.Raices de un polinomio de segundo grado 
			7.Derivar
			8.Integrar
			0.Regresar al menú principal
			""")
			opcionMenu=int(input("Opcion: "))
			
			if opcionMenu==1:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("\n\t\t\tIngresa el polinomio: "))
				b=poly(input("\n\t\t\tIngresa el polinomio: "))
				print(suma(a,b))
			
			elif opcionMenu==2:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("\n\t\t\tIngresa el polinomio: "))
				b=poly(input("\n\t\t\tIngresa el polinomio: "))
				print(resta(a,b))

			elif opcionMenu ==3:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("\n\t\t\tIngresa el polinomio: "))
				b=poly(input("\n\t\t\tIngresa el polinomio: "))
				print(multiplicacion(a,b))
				
			elif opcionMenu==4:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("\n\t\t\tIngresa el polinomio: "))
				b=poly(input("\n\t\t\tIngresa el polinomio: "))
				print(division(a,b))
			elif opcionMenu==5:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=input("\n\t\t\tIngresa el polinomio :")
				c= int(input("\n\t\t\tIngresa el número a evaluar: "))
				print("\n\n\t\t\tEl valor en ese punto del polinomio es:",Evaluar(a,c))
				
			elif opcionMenu==6:
				os.system("clear")
				polinomio=[]
				grado=int(input("\n\t\t\tIngresa el grado del polinomio:"))
				if grado==2:
					v=int(input("\n\t\t\tIngresa el coeficiente del termino cuadrado: "))
					n=int(input("\n\t\t\tIngresa el coeficiente del termino lineal : "))
					m=int(input("\n\t\t\tIngresa el coeficiente del termino independiente: "))
					polinomio.append(v)
					polinomio.append(n)
					polinomio.append(m)

				elif grado==1:
					
					n=int(input("\n\t\t\tIngresa el coeficiente del termino lineal :"))
					m=int(input("\n\t\t\tIngresa el coeficiente del termino independiente :"))
					polinomio.append(n)
					polinomio.append(m)
				else:
					print("\nSolo se pueden obtiener racíces de polinomios con grado menor o igual a 2")

				raiz(polinomio)
				
			elif opcionMenu==7:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("Ingresa el polinomio :"))
				print("La derivada del polinomio es:",derivar(a))
			elif opcionMenu==8:
				os.system("clear")
				init_printing()
				x,y=symbols('x,y')
				a=poly(input("Ingresa el polinomio: "))
				print("La integral del polinomio es: ",integrar(a))
				
			elif opcionMenu==0:
				os.system("clear")
				print("\n\n\t\t¡Hasta luego, gracias por utilizar superPoli!")
				break
			else:
				os.system("clear")
				print("Opción incorrecta, ingresa una opción válida.")
		except ValueError:
			os.system("clear")
			print("Esa opción no esta en el menú, intenta de nuevo.")
	#calcPol()