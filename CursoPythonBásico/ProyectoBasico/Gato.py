################
#Juego de Gato##	
################
import os

def tableroInicial(posicion):
	print("\n\n\n")
	print("\t\t\t\t\t\t\t         |          |          ")
	print("\t\t\t\t\t\t\t  ",posicion,"    |    ",posicion,"   |    ",posicion,"      ")
	print("\t\t\t\t\t\t\t         |          |          ")
	print("\t\t\t\t\t\t\t---------+----------+-----------")
	print("\t\t\t\t\t\t\t         |          |          ")
	print("\t\t\t\t\t\t\t  ",posicion,"    |    ",posicion,"   |    ",posicion,"      ")  
	print("\t\t\t\t\t\t\t         |          |          ")
	print("\t\t\t\t\t\t\t---------+----------+-----------")
	print("\t\t\t\t\t\t\t         |          |          ")
	print("\t\t\t\t\t\t\t  ",posicion,"    |    ",posicion,"   |    ",posicion,"      ") 
	print("\t\t\t\t\t\t\t         |          |          ")

os.system("clear")
def ComoJugar():
	print("\n\n\n")
	print("         |          |          ")
	print("  ","a","    |    ","b","   |    ","c","      ")
	print("         |          |          ")
	print("---------+----------+-----------")
	print("         |          |          ")
	print("  ","d","    |    ","e","   |    ","f","      ")  
	print("         |          |          ")
	print("---------+----------+-----------")
	print("         |          |          ")
	print("  ","g","    |    ","h","   |    ","i","      ") 
	print("         |          |          ")
	
	print("""\t\t---------------Instrucciones------------

			1.-Cada jugador ingresará su nombre y escogerá una figura (X O)
			2.-Al Inicio el jugador escoge una casilla vacía del tablero y coloca su figura en esa casilla.

			  Cada casilla del tablero tiene asignada una letra 
			  Y cada letra sera equivalente a un número:
				a=1        c=3        e=5      g=7     i=9
				b=2        d=4        f=6      h=8
			Para colocar la marca en la casilla que deseas, teclea el número equivalente a cada letra
			3.-Cuando el jugador seleccione su figura en la casilla termina su turno.
			4.-Gana el jugador que logre poner 3 figuras en una línea (vertical, horizontal o diagonal). 
				Se tacha con una línea recta las 3 figuras que forman la línea ganadora.
			5.-En el caso de que se ocupen todas las casillas y ningún jugador haya realizado una línea recta, 
			   se declara empate y se juega una nueva partida. """)

	salir=input("Presiona enter para salir")

while True:
	try:
		print(r'''				                                                                 
				  ,ad8888ba,                                          88   88    
				 d8"'    `"8b                ,d                       88   88    
				d8'                          88                     aa88aaa88aa  
				88             ,adPPYYba,  MM88MMM  ,adPPYba,       ""88"""88""  
				88      88888  ""     `Y8    88    a8"     "8a      aa88aaa88aa  
				Y8,        88  ,adPPPPP88    88    8b       d8      ""88"""88""  
				 Y8a.    .a88  88,    ,88    88,   "8a,   ,a8"        88   88    
				  `"Y88888P"   `"8bbdP"Y8    "Y888  `"YbbdP"'         88   88    
		                                                              
		                                                          						    ''')

		print("""
			    1.-Jugar
			    2.-Ver último ganador
			    3.-¿Cómo jugar?
			    4.-Salir \n\n""")
		opcion=int(input("Selecciona la opción que desees: "))
		os.system("clear")
		if opcion==1:
			os.system("clear")
			posic=[" "," "," "," "," "," "," "," "," "]
			player1=input("Ingresa el nombre del jugador 1: ")
			marca1=input('¿Qué eliges "X"  o  "O"?\t')
			player2=input("Ingresa el nombre del jugador 2: ")
			if marca1=="X" or marca1=="x":
				marca2="O" 
			elif marca1=="O" or marca1=="o":
				marca2="X" 
			while True:	
				print(player1,"es: ",marca1,"\t",player2,"es: ",marca2)
				tableroInicial(" ")
				print(player1)
				posicion=input("Ingresa tu posición: ")
				if posicion==1:
					posic[0]=marca1
					print("\t\t\t\t\t\t\t         |          |          ")
					print("\t\t\t\t\t\t\t  ",posic[0],"    |    ",posic[1],"   |    ",posic[2],"      ")
					print("\t\t\t\t\t\t\t         |          |          ")
					print("\t\t\t\t\t\t\t---------+----------+-----------")
					print("\t\t\t\t\t\t\t         |          |          ")
					print("\t\t\t\t\t\t\t  ",posic[3],"    |    ",posic[4],"   |    ",posic[5],"      ")  
					print("\t\t\t\t\t\t\t         |          |          ")
					print("\t\t\t\t\t\t\t---------+----------+-----------")
					print("\t\t\t\t\t\t\t         |          |          ")
					print("\t\t\t\t\t\t\t  ",posic[6],"    |    ",posic[7],"   |    ",posic[8],"      ") 
					print("\t\t\t\t\t\t\t         |          |          ")
					print(player1," tiró: ")
				elif posicion==2:
					posic[1]=marca1
					print(player1," tiró: ")
				elif posicion==3:
					posic[2]=marca1
					print(player1," tiró: ")
				elif posicion==4:
					posic[3]=marca1
					print(player1," tiró: ")
				elif posicion==5:
					posic[4]=marca1
					print(player1," tiró: ")
				elif posicion==6:
					posic[5]=marca1	
					print(player1," tiró: ")
				elif posicion==7:
					posic[6]=marca1
					print(player1," tiró: ")
				elif posicion==8:
					posic[7]=marca1
					print(player1," tiró: ")
				elif posicion==9:
					posic[8]=marca1
					print(player1," tiró: ")
				else:
					print("Posición incorrecta!")

				
				
				print(player2)
				posicion=input("Ingresa tu posición: ")
				if posicion==1:
					posic[0]=marca2
					print(player2," tiró: ")
				elif posicion==2:
					posic[1]=marca2
					print(player2," tiró: ")
				elif posicion==3:
					posic[2]=marca2
					print(player2," tiró: ")
				elif posicion==4:
					posic[3]=marca2
					print(player2," tiró: ")
				elif posicion==5:
					posic[4]=marca2
					print(player2," tiró: ")
				elif posicion==6:
					posic[5]=marca2	
					print(player2," tiró: ")
				elif posicion==7:
					posic[6]=marca2
					print(player2," tiró: ")
				elif posicion==8:
					posic[7]=marca2
					print(player2," tiró: ")
				elif posicion==9:
					posic[8]=marca2
					print(player2," tiró: ")
				else:
					print("Posición incorrecta!")
				
				print("\t\t\t\t\t\t\t         |          |          ")
				print("\t\t\t\t\t\t\t  ",posic[0],"    |    ",posic[1],"   |    ",posic[2],"      ")
				print("\t\t\t\t\t\t\t         |          |          ")
				print("\t\t\t\t\t\t\t---------+----------+-----------")
				print("\t\t\t\t\t\t\t         |          |          ")
				print("\t\t\t\t\t\t\t  ",posic[3],"    |    ",posic[4],"   |    ",posic[5],"      ")  
				print("\t\t\t\t\t\t\t         |          |          ")
				print("\t\t\t\t\t\t\t---------+----------+-----------")
				print("\t\t\t\t\t\t\t         |          |          ")
				print("\t\t\t\t\t\t\t  ",posic[6],"    |    ",posic[7],"   |    ",posic[8],"      ") 
				print("\t\t\t\t\t\t\t         |          |          ")
				



	
	



















				break
		elif opcion==2:
			os.system("clear")
			pass
		elif opcion==3:
			os.system("clear")
			ComoJugar()
		elif opcion==4:
			os.system("clear")
			print("Regresa Pronto :) ")
			break
		else:
			os.system("clear")
			print("No es válido, ingresa una opción correcta")
	except ValueError:
		os.system("clear")
		print("Ese no es un número para seleccionar la opción")










