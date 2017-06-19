###
#Listas
###


lista=["hola",4,10.4,True]
lista2=["a",10,[1,2,3]]

print("Tipo de dato: ",type(lista))
print("Indexacion: ",lista[0]) # indeces por cada uno de los elementos de la lista, siempre empieza en 0
print("Longitud: ",len(lista))
print("Concatenacion: ",lista+lista2) # Si fuera una cadena, lo tendriamos que castear a lista para qie se puedan sumar 

lista[0]="Hola"
print(lista[0])
print("Busqueda: ", 3 in lista2)
#sublista
print(lista2[2][1])
print("Elemento en sublista: ",lista2[2][1])

for elemento in lista:
	print("Elemento: ",elemento)

print("Slicing: ",lista[1:3])
print("Slicing: ",lista[-1:-3])
#Brincos de las cadenas [inicio:fin:salto]
print("Slicing: ",lista[ 0: :2])
#es cuando pones en sentido contrario la cadena 
print("Slicing: ",lista[ : :-1])

#Operaciones
lista=["A","B","C","D"]
lista.append("E")	
print(lista)
lista.insert(0,"Z")
print(lista)
ultimoElemento=lista.pop()
print(ultimoElemento)
print(lista)
#Eliminacion del elemento
del lista[0]
print(lista)
lista2=[3,4,1,5,8,2]
print("Maximo: ",max(lista2))
print("Minimo: ",min(lista2))
#Ordenamiento
lista2.sort()
print("Lista ordenada: ",lista2)
lista2.reverse()
print("Lista en orden inverso: ",lista2)
#indice de un elemento
print("Indice de B: ",lista.index("B"))

