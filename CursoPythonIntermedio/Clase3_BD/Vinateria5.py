#*-* coding:utf-8 *-*
import sqlite3, datetime#Importamos la libreria
#Conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite3")#nombre de la carpeta/nombre del script
#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()
#Definimos nuestra consulta con la observacion de cuidar las "" en la query
sql="UPDATE bebida SET nombre= \"Jack\" WHERE id_bebida = %s" %3
#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Registro modificado con exito :D")
else:
	print("Error al hacer la modificacion :S")

sql="UPDATE bebida SET precio= \"1500\" WHERE id_bebida = %s" %3
#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Registro modificado con exito :D")
else:
	print("Error al hacer la modificacion :S")

sql= "DELETE FROM bebida WHERE id_bebida=%s" %3 
if(consulta.execute(sql)):
	print("Registro borrado con exito :D")
else:
	print("Error al hacer la eliminacion :S")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexion a la base de datos
conexion.close()
