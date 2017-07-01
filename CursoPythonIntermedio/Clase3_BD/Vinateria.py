import sqlite3, datetime#Importamos la libreria
#Recibimos los valores que el usuario quiere almacenar
print("******************Bienvenido*********************")
nombre=input("Introduzca el nombre de la bebida: ")
precio=input("Introduzca el precio de la bebida: ")

try:
	precio=float(precio) or int(precio)
except ValueError:
	print(precio, "no es un numero entero flotante")
	exit()
conexion=sqlite3.connect("chelas.sqlite3")

consulta=conexion.cursor()
#Almacenando los datos en una tupla
argumentos=(nombre,precio,datetime.date.today())#yyyy-yy-dd
#Creando string con la consulta insert SQL
sql="""
INSERT INTO bebida(nombre,precio,exportacion)
VALUES(?,?,?)
"""
if(consulta.execute(sql,argumentos)):
	print("Registro guardado con exito :D")
else:
	print("Error al guardae el regsitro :S")
#Terminamos la consulta
consulta.close()
conexion.commit()
conexion.close()