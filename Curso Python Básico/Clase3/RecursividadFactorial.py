###

### 8!=8x7x6x5x4x3x2x1

def factorial(num):     #definicion
	if num<1:
		return 1         # Condicion de paro
	else:					#2*1*1
		return num*factorial(num-1)    #Llamando a la funcion 
a=int(input("De que numero quiere saber su factorial?"))

print(factorial(a))


############################ FORMA ITERATIVA####################
def factorial2(num):
	fack=1
	for i in range(2,num+1):
		fack*=i
	return fack

print(factorial2(5))

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(60))
print(factorial(70))
print(factorial(997))

import sys
print("Limite de llamadas: ", sys.getrecursionlimit())
#CUIDADO NO TOCAR
#sys.setrecursionlimit(1002)
print("Limite de llamadas: ",sys.getrecursionlimit())

def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else: 
		return fibo(n-1)+fibo(n-2)

print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))


