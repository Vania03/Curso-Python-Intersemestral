
import os
#Con este limpiamos la pantalla
os.system("clear")
#Declaramos un diccionario vacio para guardar los contactos
contactos={}
print("\n\n\t\t\t\t\t\t\t\tBienendio a la Super Agena")

while True:
	print("Selecciona la opcion que desea realizar: ")
	print("\n\t1.-Agregar un contacto. ")
	print("\n\t2.-Buscar un contacto. ")
	print("\n\t3.-Ver todos los contactos. ")
	print("\n\t4.-Eliminar contactos. ")
	print("\n\t5.-Salir. ")

	opcionMenu=int(input("Opcion: "))
	if opcionMenu==1:
		#Agregar contacto
		nombre=input("\n\n\t Ingresa el nombre del contacto: ")
		numero=int(input("Ingresa el numero de telefono: "))
		contactos[nombre]=numero
		os.system("clear")
	elif opcionMenu==2:
		#Buscar un numero
		nombre=input("¿Que contacto deseas buscar?: ")
		os.system("clear")
	if nombre in contactos:
		print("\n Nombre: ",nombre)
		print("\n Telefono: ",contactos[nombre])
	else:
		print("\nError 404, contacto no encontrado")
		#Ver todos los contactos
	elif opcionMenu==3:
	os.system("clear")
	if len(contactos.items())==0:
		print("\n\n\tNo hay contactos para mostrar!")
	else:
		for persona in contactos.keys():
			print("\n\n\tEl numero de  ",persona,"es: ", contactos[persona])
elif opcionMenu ==4:
	#Eliminar contacto
	nombre=input("¿Que contacto deseas borrar?: ")
	os.system("clear")
	if nombre in contactos:
		del contactos[nombre]
	else opcionMenu==5:
		#Para salir
		os.system("clear")

