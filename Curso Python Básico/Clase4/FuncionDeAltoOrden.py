###
#Funciones de alto oreden 
###


items = list((1,11))
print(items)

cuadrados=[]

def cuadrado(x):
	return x**2

cuadrados= list(map(cuadrado, items))

print(cuadrados)

#Ahora con Lambda
cubos= list(map(lambda x:x**3,items))

print(cubos)

###
#Filter
###

multiplos4= list(filter(lambda n:n%4!=0, items))

print(multiplos4)


###
#Reduce
##
#Importamos la funcion reduce, ya que python 3 ya no lo tiene por ello hay que importar funciones de modulos
#Reduce: Reduce una lista a un elemento. Resume la lista y aplica la funcion y asegirarnos de que todos los elementos sean aplicables 
import functools
res=reduce(lambda a,b:a+b,items)
print(res)

###
#Lambda
###

#Lamda parametros:Funciones

#def f(a,b):
# return a+b

f=lambda a,b:a+b

print("Resultado", f(1,1))
