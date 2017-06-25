#-*-coding:utf-8-*-
####################################
##CALCULADORA DE POLINOMIOS##
####################################
import os
import math

def sumaC():

	
	a=complex(input("\nIngresa el primer número: "))
	b=complex(input("Ingresa el segundo número: "))

	print("\n\t\tLa suma de: ",a,"y :",b,"es: ",a+b,"\n")
	
	
def restaC():
	
	
	a=complex(input("\nIngresa el primer número: "))
	b=complex(input("Ingresa el segundo número: "))

	print("\n\t\tLa resta de: ",a,"y :",b,"es: ",a-b,"\n")

def multiC():
	
	
	a=complex(input("\nIngresa el primer número: "))
	b=complex(input("Ingresa el segundo número: "))

	print("\n\t\tLa multiplicación de: ",a,"y :",b,"es: ",a*b,"\n")

def diviC():
	
	
	a=complex(input("\nIngresa el primer número: "))
	b=complex(input("Ingresa el segundo número: "))

	print("\n\t\tLa división de: ",a,"entre :",b,"es: ",a/b,"\n")

def modAngC():
	
	a=complex(input("\nIngresa el número que quieres transformar: "))
	ang=math.degrees(math.atan(a.imag/a.real))
	print("El resultado es: ",abs(a)," |_",ang)
def potenciaC():
	
	pass
def raizC():
	pass
def polarC():
	
	a=complex(input("\nIngresa el número que quieres transformar: "))
	r=math.sqrt(pow(a.real,2)+pow(a.imag,2))
	ang=math.degrees(math.atan(a.imag/a.real))
	print("La magnitud es: ",r," y el ángulo es: ",ang,".")

	pass



def Complejos():
	os.system("clear")
	print("""		                  ___                             _                
                                 (  _`\                          (_ )              
  ___  _   _  _ _      __   _ __ | ( (_)   _     ___ ___   _ _    | |    __        
/',__)( ) ( )( '_`\  /'__`\( '__)| |  _  /'_`\ /' _ ` _ `\( '_`\  | |  /'__`\(`\/')
\__, \| (_) || (_) )(  ___/| |   | (_( )( (_) )| ( ) ( ) || (_) ) | | (  ___/ >  < 
(____/`\___/'| ,__/'`\____)(_)   (____/'`\___/'(_) (_) (_)| ,__/'(___)`\____)(_/\_)
             | |                                          | |                      
             (_)                                          (_)                      
		""")
	while True:	
		try:
			print("\nTus números deben ser de la forma: a+ bj donde a y b son números y j es la letra imaginaria.\n")
			print("\n\t\t\t\t\tSelecciona la opción que deseas realizar")
			print("""\t\t\t\t\t
					  \t\t1.-Sumar
					  \t\t2.-Restar
					  \t\t3.-Multiplicar
					  \t\t4.-Dividir
					  \t\t5.-Modulo y ángulo
					  \t\t6.-Potenciación
					  \t\t7.-Raíz enésima
					  \t\t8.-Forma polar
					  \t\t0.-Ir al menú principal
				""")
			opcion=int(input("\t\t\t\t\tOpción: "))
			os.system("clear")
			if opcion==1:
				os.system("clear")
				sumaC()
			elif opcion==2:
				os.system("clear")
				restaC()
			elif opcion==3:
				os.system("clear")
				multiC()
			elif opcion==4:
				os.system("clear")
				diviC()
			elif opcion==5:
				os.system("clear")
				modAngC()
			elif opcion==6:
				os.system("clear")
				potenciaC()
			elif opcion==7:
				os.system("clear")
				raizC()
			elif opcion==8:
				os.system("clear")
				polarC()
			elif opcion==0:
				os.system("clear")
				print("\n\n\t\t¡Hasta luego, gracias por utilizar superComplex!")
				break
				pass
			else: 
				os.system("clear")
				print("Opción incorrecta, ingresa una opción válida.")
		except ValueError:
			os.system("clear")
			print("¡Ese no es un número, intenta de nuevo!")

Complejos()	