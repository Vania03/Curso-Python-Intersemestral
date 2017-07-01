#-*-coding:utf-8-*-
import os
from calcComplejos import Complejos
from calcPoli import calcPol
from Gato import Gatuno

while True:
	try:

		print(r''' 
			     ___           _    _                       ___                                  
		            (  _`\        ( )_ ( )                     (  _`\               _               
		            | |_) ) _   _ | ,_)| |__     _     ___     | (_) )   _ _   ___ (_)   ___    _   
		            | ,__/'( ) ( )| |  |  _ `\ /'_`\ /' _ `\   |  _ <' /'_` )/',__)| | /'___) /'_`\ 
		            | |    | (_) || |_ | | | |( (_) )| ( ) |   | (_) )( (_| |\__, \| |( (___ ( (_) )
		            (_)    `\__, |`\__)(_) (_)`\___/'(_) (_)   (____/'`\__,_)(____/(_)`\____)`\___/'
		                   ( )_| |                                                                  
		                   `\___/'                                                 _                
		                     /'\_/`\ _                                            ( )_              
		                     |     |(_)    _ _    _ __   _    _   _    __     ___ | ,_)   _         
		                     | (_) || |   ( '_`\ ( '__)/'_`\ ( ) ( ) /'__`\ /'___)| |   /'_`\       
		                     | | | || |   | (_) )| |  ( (_) )| (_) |(  ___/( (___ | |_ ( (_) )      
		                     (_) (_)(_)   | ,__/'(_)  `\___/'`\__, |`\____)`\____)`\__)`\___/'      
		                                  | |                ( )_| |                                
		                                  (_)                `\___/'                                '''"\n")

			              




		print("\n\t\t1.-Calculadora de Complejos")
		print("\n\t\t2.-Calculadora de Polinomios")
		print("\n\t\t3.-Juego del Gato")
		print("\n\t\t0.-Salir")


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
			print(''' 
				         _                _             _          _            _        
				        / /\             /\ \          /\ \       /\ \         / /\      
				       / /  \           /  \ \____     \ \ \     /  \ \       / /  \     
				      / / /\ \         / /\ \_____\    /\ \_\   / /\ \ \     / / /\ \__  
				     / / /\ \ \       / / /\/___  /   / /\/_/  / / /\ \ \   / / /\ \___\ 
				    / / /  \ \ \     / / /   / / /   / / /    / / /  \ \_\  \ \ \ \/___/ 
				   / / /___/ /\ \   / / /   / / /   / / /    / / /   / / /   \ \ \       
				  / / /_____/ /\ \ / / /   / / /   / / /    / / /   / / /_    \ \ \      
				 / /_________/\ \ \\ \ \__/ / /___/ / /__  / / /___/ / //_/\__/ / /      
				/ / /_       __\ \_\\ \___\/ //\__\/_/___\/ / /____\/ / \ \/___/ /       
				\_\___\     /____/_/ \/_____/ \/_________/\/_________/   \_____\/        
				                                                                         ''')
			break
		else:
			os.system("clear")
			print("\n\n\tOpción no válida, intenta de nuevo!")
	except ValueError():
		print("Esto no es un numero, intenta de nuevo")


		