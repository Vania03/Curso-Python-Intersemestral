#*_* coding: utf-8 *_*
import sqlite3#Importamos la libreria
#Hacer relacion nombre de la carpeta\extension del archivo script sqlite3
#Asignar ocnexcion a una variable llamada conexion
#Conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite3")

#El acceso a base de datos se define de modo estandar en las especificaciones DB-API (PEP 249)
#Seleccionamos el cursos para realizr la consulta
consulta=conexion.cursor()
#Estamos creando un String con la consulta SQL
sql="""
CREATE TABLE IF NOT EXISTS bebida(
id_bebida INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
nombre VARCHAR(50) NOT NULL,
precio FLOAT NOT NULL,
exportacion DATE NOT NULL
)"""
#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Tabla creada con exito :D")
else:
	print("Error al crear la tabla :S")
#Terminamos la consulta
consulta.close()
#Guardamos los cambioes en la base de datoa
conexion.commit()
#
conexion.close()



