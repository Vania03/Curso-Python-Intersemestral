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

def ganador(players,player1,player2,marca1,marca2,posic):
		#########################SI PLAYER1=X
		if players[player1]=="X":
			###############HORIZONTALES
			if posic[0]=="X" and posic[1]=="X" and posic[2]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[3]=="X" and posic[4]=="X" and posic[5]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[6]=="X" and posic[7]=="X" and posic[8]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			##############VERTICALES
			elif posic[0]=="X" and posic[3]=="X" and posic[6]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[1]=="X" and posic[4]=="X" and posic[7]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[2]=="X" and posic[5]=="X" and posic[8]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			################DIAGONALES
			elif posic[0]=="X" and posic[4]=="X" and posic[8]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[2]=="X" and posic[4]=="X" and posic[6]=="X":
				print("¡ ",player1," ha ganado!")
				return True
			else:
				###############HORIZONTALES
				if players[player2]=="O":
					if posic[0]=="O" and posic[1]=="O" and posic[2]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[3]=="O" and posic[4]=="O" and posic[5]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[6]=="O" and posic[7]=="O" and posic[8]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					##############VERTICALES
					elif posic[0]=="O" and posic[3]=="O" and posic[6]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[1]=="O" and posic[4]=="O" and posic[7]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[2]=="O" and posic[5]=="O" and posic[8]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					################DIAGONALES
					elif posic[0]=="O" and posic[4]=="O" and posic[8]=="O":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[2]=="O" and posic[4]=="O" and posic[6]=="O":
						print("¡ ",player2," ha ganado!")
						return True
		####################SI PLAYER1=O
		elif players[player1]=="O":
			###############HORIZONTALES
			if posic[0]=="O" and posic[1]=="O" and posic[2]=="O":
				print("¡ ",player1," ha ganado!")
				return True

			elif posic[3]=="O" and posic[4]=="O" and posic[5]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[6]=="O" and posic[7]=="O" and posic[8]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			##############VERTICALES
			elif posic[0]=="O" and posic[3]=="O" and posic[6]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[1]=="O" and posic[4]=="O" and posic[7]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[2]=="O" and posic[5]=="O" and posic[8]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			################DIAGONALES
			elif posic[0]=="O" and posic[4]=="O" and posic[8]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			elif posic[2]=="O" and posic[4]=="O" and posic[6]=="O":
				print("¡ ",player1," ha ganado!")
				return True
			else:
				###############HORIZONTALES
				if players[player2]=="X":
					if posic[0]=="X" and posic[1]=="X" and posic[2]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[3]=="X" and posic[4]=="X" and posic[5]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[6]=="X" and posic[7]=="X" and posic[8]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					##############VERTICALES
					elif posic[0]=="X" and posic[3]=="X" and posic[6]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[1]=="X" and posic[4]=="X" and posic[7]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[2]=="X" and posic[5]=="X" and posic[8]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					################DIAGONALES
					elif posic[0]=="X" and posic[4]=="X" and posic[8]=="X":
						print("¡ ",player2," ha ganado!")
						return True
					elif posic[2]=="X" and posic[4]=="X" and posic[6]=="X":
						print("¡ ",player2," ha ganado!")
						return True


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
			    2.-¿Cómo jugar?
			    3.-Salir \n\n""")
		opcion=int(input("Selecciona la opción que desees: "))
		os.system("clear")
		if opcion==1:
			os.system("clear")
			posic=[" "," "," "," "," "," "," "," "," "]
			players={}
			player1=input("\n\tIngresa el nombre del jugador 1: ")
			marca1=input('\n\t¿Qué eliges "X"  o  "O"?   ')
			player2=input("\n\tIngresa el nombre del jugador 2: ")
			os.system("clear")
			if marca1=="X" or marca1=="x":
				marca1=marca1.upper()
				marca2="O" 
			elif marca1=="O" or marca1=="o":
				marca2="X"
				marca2=marca2.upper()
			else:
				print("No es una marca válida!")
				break
			players[player1]=marca1
			players[player2]=marca2
			#print(players)
			tableroInicial(" ")
			##############################INICIO DEL JUEGO################
			while True:
				print("\n\t\t\t\t\t\t",player1,"es: ",marca1,"\t",player2,"es: ",marca2)
				print(player1)
				termina=ganador(players,player1,player2,marca1,marca2,posic)	
				if termina==True:
					break
				else:
					posicion=int(input("Ingresa tu posición: "))
					os.system("clear")
					print("\n\t\t\t",player1,"es: ",marca1,"\t",player2,"es: ",marca2)
					if posicion==1:
						if posic[0]=="X" or posic[0]=="x" or posic[0]=="O" or posic[0]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[0]=marca1
							os.system("clear")
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==2:
						if posic[1]=="X" or posic[1]=="x" or posic[1]=="O" or posic[1]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[1]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==3:
						if posic[2]=="X" or posic[2]=="x" or posic[2]=="O" or posic[2]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[2]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==4:
						if posic[3]=="X" or posic[3]=="x" or posic[3]=="O" or posic[3]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[3]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==5:
						if posic[4]=="X" or posic[4]=="x" or posic[4]=="O" or posic[4]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[4]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==6:
						if posic[5]=="X" or posic[5]=="x" or posic[5]=="O" or posic[5]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[5]=marca1
							os.system("clear")	
							print(player1," tiró: ")
					elif posicion==7:
						if posic[6]=="X" or posic[6]=="x" or posic[6]=="O" or posic[6]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[6]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==8:
						if posic[7]=="X" or posic[7]=="x" or posic[7]=="O" or posic[7]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[7]=marca1
							os.system("clear")
							print(player1," tiró: ")
					elif posicion==9:
						if posic[8]=="X" or posic[8]=="x" or posic[8]=="O" or posic[8]=="o":
							print("Ya esta ocupado ese lugar, pierdes un turno!")
						else:
							posic[8]=marca1
							os.system("clear")
							print(player1," tiró: ")
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
					if posic[0]!=" " and posic[1]!=" " and posic[2]!=" " and posic[3]!=" " and posic[4]!=" " and posic[5]!=" " and posic[6]!=" " and posic[7]!=" " and posic[8]!=" ":
						print("¡Empate, nadie gana!")
						break
					else:
						termina2=ganador(players,player1,player2,marca1,marca2,posic)	
						if termina2==True:
							break
						else:
							print(player2)
							posicion=int(input("Ingresa tu posición: "))
							os.system("clear")
							print("\n\t\t\t",player1,"es: ",marca1,"\t",player2,"es: ",marca2)
							if posicion==1:
								if posic[0]=="X" or posic[0]=="x" or posic[0]=="O" or posic[0]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[0]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==2:
								if posic[1]=="X" or posic[1]=="x" or posic[1]=="O" or posic[1]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[1]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==3:
								if posic[2]=="X" or posic[2]=="x" or posic[2]=="O" or posic[2]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[2]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==4:
								if posic[3]=="X" or posic[3]=="x" or posic[3]=="O" or posic[3]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[3]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==5:
								if posic[4]=="X" or posic[4]=="x" or posic[4]=="O" or posic[4]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[4]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==6:
								if posic[5]=="X" or posic[5]=="x" or posic[5]=="O" or posic[5]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[5]=marca2
									os.system("clear")	
									print(player2," tiró: ")
							elif posicion==7:
								if posic[6]=="X" or posic[6]=="x" or posic[6]=="O" or posic[6]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[6]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==8:
								if posic[7]=="X" or posic[7]=="x" or posic[7]=="O" or posic[7]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[7]=marca2
									os.system("clear")
									print(player2," tiró: ")
							elif posicion==9:
								if posic[8]=="X" or posic[8]=="x" or posic[8]=="O" or posic[8]=="o":
									print("Ya esta ocupado ese lugar, pierdes un turno!")
								else:
									posic[8]=marca2
									os.system("clear")
									print(player2," tiró: ")
							else:
								print("Posición incorrecta!")
							print("\t\t\t\t\t\t\t         |          |          ")
							print("\t\t\t\t\t\t\t  ",posic[0],"    |    ",posic[1],"   |    ",posic[2],"      ")
							print("\t\t\t\t\t\t\t         |          |          ")
							print("\t\t\t\t\t\t\t --------+----------+-----------")
							print("\t\t\t\t\t\t\t         |          |          ")
							print("\t\t\t\t\t\t\t  ",posic[3],"    |    ",posic[4],"   |    ",posic[5],"      ")  
							print("\t\t\t\t\t\t\t         |          |          ")
							print("\t\t\t\t\t\t\t---------+----------+-----------")
							print("\t\t\t\t\t\t\t         |          |          ")
							print("\t\t\t\t\t\t\t  ",posic[6],"    |    ",posic[7],"   |    ",posic[8],"      ") 
							print("\t\t\t\t\t\t\t         |          |          ")
							
				#Posibilidades de ganar:
				
					
			#print(posic)	
		elif opcion==2:
			os.system("clear")
			ComoJugar()
		elif opcion==3:
			os.system("clear")
			print("Regresa Pronto :) ")
			break
		else:
			os.system("clear")
			print("No es válido, ingresa una opción correcta")
	except ValueError:
		os.system("clear")
		print("Ese no es un número para seleccionar la opción")









