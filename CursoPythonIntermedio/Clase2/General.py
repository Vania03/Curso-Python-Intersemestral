##

import math

class Imaginario(Exception):
	pass
class Polinomio(Exception):
	pass

def func(a,b,c):
	try:
		if a==0:
			raise Polinomio
		elif b**2 -4*a*c<0:
			raise Imaginario
		else:
			print("x1: ",(-b+math.sqrt(b**2 -4*a*c))/(2*a))
			print("x2: ",(-b+math.sqrt(b**2 -4*a*c))/(2*a))
	except Polinomio:
			print("No es una ecuacion de segundo grado :( ")
	except Imaginario:
			print("Si hay raices, pero son complejas! ")

func(1,4,2)
			


		