#
#Archivos
#

#open(rutaDelArchivo,modo)#modo por default en solo lectura

#archivo=open(r"D:\UsersArchivos.txt", "r")
archivo=open("Archivos.txt", "a+")
print("Nombre del arcbhivo: ",archivo.name)
print("Modo de Apertura: ",archivo.mode)

#siempre por buenas practicas deben cerrarse todos los archivos o flujos de datos
#archivo.close()

if archivo.closed:
	print("El archivo esta cerrado")
else:
	print("El archivo esta abierto")
#lee el contenido del texto como una cadena
#texto=archivo.read()
#print(texto)
#checar tipo de texto con type
#print(type(texto))

texto=input("Ingresa texto para escribir en el archivo: ")
archivo.write("\n"+texto)

#Mover el apuntador
archivo.seek(0)#bytes . Un caracter = 4 bytes
print("Contenido del archivo: ",archivo.read())

#archivo.closed()

#Manejador de contexto, cierra el archivo por deafault, mas legible
with open(input("Ingrese el nombre del archivo: ")) as f:
	lineas=f.readlines()

print(lineas)
for linea in lineas:
	print(linea,end="")

"""archivo=open("Archivos2.txt", "w")
print("Nombre del arcbhivo: ",archivo.name)
print("Modo de Apertura: ",archivo.mode)

#siempre por buenas practicas deben cerrarse todos los archivos o flujos de datos
#archivo.close()

if archivo.closed:
	print("El archivo esta cerrado")
else:
	print("El archivo esta abierto")
#lee el contenido del texto como una cadena
#texto=archivo.read()
#print(texto)
#checar tipo de texto con type
#print(type(texto))

texto=input("Ingresa texto para escribir en el archivo: ")
archivo.write(texto)

archivo.closed"""
