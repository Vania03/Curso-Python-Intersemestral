import random

numeroadivinador=random.randrange(1,10)
#print(numeroadivinador)
while True:
	numeroInsertado=int(input("Adivina un numero entro el 1 y el 9: \nNumero:"))
	if numeroInsertado==numeroadivinador:
		print("Tu numero: ",numeroInsertado," es igual al numero que tenia en mente: ",numeroadivinador,"\t GANASTE!!!!")
		break
	else:
		print("Tu numero: ", numeroInsertado," es diferente al numero que tenia en mente: \t INTENTA DE NUEVO")


		



