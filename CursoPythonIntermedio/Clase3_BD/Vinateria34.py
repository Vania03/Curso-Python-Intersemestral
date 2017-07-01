import sqlite3, datetime
conexion=sqlite3.connect("chelas.sqlite3")

consulta=conexion.cursor()
sql="""SELECT * FROM bebida"""

if (consulta.execute(sql)):
	filas=consulta.fetchall()
	for fila in filas:
		print (fila[0], fila[1], fila[2], fila[3])
#Redefinimos nuestra consulta con un formato diferente 
sql="SELECT * FROM bebida WHERE id_bebida=%s" %2

#Ejecutamos la consulta. Extrayendo una sola fila (Registro)
consulta.execute(sql)
fila=consulta.fetchone()
print ("Seleccionamos del registro con id 2..: ", fila[0], fila[1], fila[2], fila[3])
#Redefinimos nuestra consulta tomando las columnas especificadas
sql="SELECT nombre, precio FROM bebida"

consulta.execute(sql)
filas=consulta.fetchall()
for fila in filas:
	print (fila[0], fila[1])

consulta.close()
conexion.commit()
conexion.close()