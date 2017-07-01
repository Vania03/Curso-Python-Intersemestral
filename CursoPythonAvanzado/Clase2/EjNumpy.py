##########
#Ej Numpy
#########

import numpy as np 
#Objeto principal con el que trabajaremos, como es un objeto tiene atributos
a=np.array([1,2,3])
print("Tipo de dato: ", type(a))
print("Dimension: ",a.shape)
print("Indexacion: ",a[0],a[1],a[2])
a[0]=5 #Asignacion por ITEM
print("Dato: ",a[0])
print("Imprimir el array ",a)
#Para una dimension de 2 ([][])
b= np.array([[1,2,3],[4,5,6]])
print("Tipo de dato: ", type(b))
print("Dimension: ",b.shape)
print("Indexacion: ",b[0,0],b[0,1],b[1,0])#1 2 4

#Funciones para generar espacios de numeros

a= np.arange(10)#0......9
print(a)
b = np.arange(0,11,2)#inicio,fin,saltos  0.....11 dos en dos
print(b)

#linspace, para saltos
c=np.linspace(0,1,6)#inicio, fin, NO.puntos queremos(que contenga 6 elementos)
print(c) #Es inclusivo

d = np.linspace(0,1,5,endpoint=False)
print(d)#No es inclusivo

e = np.linspace(0,1,101)
print(e)


#Funciones para crear matrices

a = np.zeros((2,2))#Incializarla con ceros
print(a)

b = np.ones((2,2))#Incializarla con uno
print(b)
#Para arreglar arreglo con una constante
c = np.full((2,2),7)
print(c)

d = np.eye(2)#Incializarlos con la identidad (eye)
print(d)

e = np.random.random((2,2))#incializarlo con numeros pseudoaleatorios
print(e)

#Matriz del 1 al 12 (3,4)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Slicing en nparrays es de esta forma:
b=a[ :2,1:3]
print(b)

print("-> ",a[0,1])#2
b[0,0]=77
print(a[0,1])
print (a)


#Tipos de datos numericos


x=np.array([1,2])
print(x.dtype)

y=np.array([1.0,2.0])
print(y.dtype)#dtype para poner el tipo de dato que queremos

#Operaciones con matrices

x=np.array([[1,2],[3,4]],dtype=np.float64)
x=np.array([[5,6],[7,8]],dtype=np.float64)
#Elemento a elemneto
print("Suma: ",x+y)
print("Resta: ",np.subtract(x,y))

print("Multiplicacion: ",x*y)

print("Division: \n",x/y)
print("Raiz: \n",np.sqrt(x))

#Multiplicacion de matrices
v=np.array([9,10])
w=np.array([11,12])
#Producto punto
print("Producto punto: ",v.dot(w))

print(x.dot(v))
#Producto Matricial
print("Prodcuto Matricial: ",np.dot(x,v))
#x * y
print("x*y:\n",x.dot(y))


print("x*I:\n",x.dot(np.eye(2)))

#x^-1

inversaX=np.linalg.inv(x)

print("Inversa de X: \n",inversaX)

print("x*x^-1:\n",x.dot(inversaX))


#Determinante
determinante=np.linalg.det(x)
print("Determinante de X: \n",determinante)
print("Transpuesta de X: \n",x.transpose())






