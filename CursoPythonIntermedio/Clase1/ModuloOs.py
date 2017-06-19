###
#Modulo Os
##
#nos perimte interactuar con el sistema operativo

import os
#Conocer el nombre del sistema o entorno en el que corre python
print("Nombre del sistema operarivo: ",os.name)
#Invocar un comando externo
os.system("ls")
#Saber el diccionario actual
print("Directorio actual: ",os.getcwd())
#Caracterisitcas del sistema
print(os.uname())
#Listar un directorio
#. = directotio actual
#.. = directorio padre
print(os.listdir)
#Eliminar carpeta
os.rmdir("Nueva Carpeta")
#crear un directorio
os.mkdir("Nueva Carpeta")

#Cambiarnos de directorio
os.chdir("Nueva Carpeta")
print("directorio actual: ",os.getcwd())

os.chdir("..")
#os.rename(src,dst)
os.rename("Nueva Carpeta","Carpeta Renombrada")
print(os.listdir("."))
os.rmdir("Carpeta Renombrada")
