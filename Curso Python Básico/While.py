###
#while
###

a=0
b=3

while a<10:
	print(("%d * %d = %d")%(a,b,a*b))
	a=a+1 #a+=1
print("Se termino el ciclo :(")


a=0
b=int(input("Ingresa el numero que desea saber su tabla de multiplicacion"))

while a<10:
	print(("%d * %d = %d")%(a,b,a*b))
	a=a+1 #a+=1
print("Se termino el ciclo :(")

#while con break y continue

a=0

while a<10:
	a=a+1
	if a==2:     #Se salta la interacion del numero 2
		continue 
	elif a==5:   #Ya no llego al 5, se quedo en el 4
		break
	print(a)
print("Se termino el segundo ciclo")