###
#tuplas
###

tupla=("hola",1,10,True)
tupla2=["a",10,[1,2,3]]
tuplaVacia=()
sigleton=(1,)


print("Tipo de dato: ",type(tupla))
print("Indexacion: ",tupla[0])
print("Longitud: ",len(tupla))
print("Concatenacion: ",tupla+tupla2)

#No permite porque la tupla es inmutable
#tupla[0]="Hola"

tupla2[2][1]=0
print(tupla2)
#Cuando dentro de una tupla hay una lista si puedo cambiar la tupla, siempre y cuando sus elemntos que la contienen son inmutables

