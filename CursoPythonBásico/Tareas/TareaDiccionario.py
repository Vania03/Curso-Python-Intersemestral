###
#Agenda Telefonica tarea
###


directorio={"Julio":5534567687,"Gabriela":5535714785,"Marla":5523015969,"Oscar":5545678734,"Fatima":5544335645}

print("El numero telefonico de Julio es: ",directorio["Julio"])
print("El numero telefonico de Gabriela es: ",directorio["Gabriela"])
print("El numero telefonico de Marla es: ",directorio["Marla"])
print("El numero telefonico de Oscar es: ",directorio["Oscar"])
print("El numero telefonico de Fatima es: ",directorio.get("Fatima"))
print("El numero telefonico de Luis es: ",directorio.get("Luis"))
print("El numero telefonico de Luis es: ",directorio.get("Luis","No existe contacto"))

#Agregar contacto
directorio["Luis"]=556445644
print(directorio)

"Gabriela" in directorio




correo={"Julio":"julio_@gmail.com","Gabriela":"gabriela_@gmail.com","Marla":"marla_@gmail.com","Oscar":"oscar_@gmail.com","Fatima":"fat_@gmail.com"}

print("El correo electronico de Julio es: ",correo["Julio"])
print("El correo electronico de Gabriela es: ",correo["Gabriela"])
print("El correo electronico de Marla es: ",correo["Marla"])
print("El correo electronico de Oscar es: ",correo["Oscar"])
print("El correo electronico de Fatima es: ",correo["Fatima"])


#Agregar correo de nuevo contacto
correo["Luis"]="luis_@gmail.com"
print(correo)

for persona in directorio.keys():
	print("El numero telefonico de ",persona,"es",directorio[persona], "Y su correo electronico es :",correo[persona])

#Cuando aun no agregaba al nuevo contacto "Luis", para esta operacion de for in,
#solo aparecia en el directorio hasta el nombre de Fatima, pero cuando ya agregue
#los datos del nuevo contacto como su numero telefonico y su correo ya se podian 
#visualizar como los demas elemetos
directorio.keys()
print(directorio)

print(directorio.items())


#Aqui se muestra todo el directorio

for persona in directorio:
	print(persona)



