###
#Diccionario	
###

diccionario={"a":0,"b":1,"c":2,"d":True,"e":[1,2,3]}
print(diccionario["a"])
print(diccionario["b"])
print(diccionario["c"])
print(diccionario["d"])
print(diccionario["e"])

#no se puede porque una lista no  puede ser una llave porque no es inmutable
diccionario2={[1,2,3]:"a"}
#Asi seria lo correcto como una tupla 
diccionario2={{1,2,3}:"a"}

calificaciones={"alan":10,"coral":6,"jorge":5}
print("calificacion de alan: ",calificaciones["alan"])
print("calificacion de alan: ",calificaciones.get["alan"])
#print("calificacion de luis: ",calificaciones["luis"])
print("calificacion de luis: ",calificaciones.get["luis"])
#Valor por default
print("calificacion de luis: ",calificaciones.get["luis",0])
#Modificar valor
calificaciones["coral"]=8
print(calificaciones["coral"])
#Crear un valor
calificaciones["luis"]=8
print(calificaciones["luis"])

print(calificaciones)

for persona in calificaciones.keys():
	print("Calificacion de ",persona,"es",calificaciones[persona])

print(calificaciones.values())
print(calificaciones.items())
