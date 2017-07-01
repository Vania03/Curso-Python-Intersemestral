#-*-coding:utf-8-*-
#Modulo que nos va a permitir enviar correos electronicos desde python3
import smtplib
#To, es quien sera enviado el correo
to='jorgechavez.proteco@gmail.com'
#Datos de quien enviara el correo
gmail_User='cursopython.proteco@gmail.com'
gmail_Pass='python.isCool'
#metodo SMTP recibe el nombre del servidor al que vamos a pedirle que nos 
#permita enviar el correo y ademas su puerto
smtpserver=smtplib.SMTP('smtp.gmail.com',587)
#Con el metodo ehlo saludamos al servidor
smtpserver.ehlo()
#Aqui comenzamos la transferencia, si es que nos reconocio
smtpserver.starttls()

##################Logueo en gmail
#El metodo nos va a permitir loguearnos en gmail
smtpserver.login(gmail_User,gmail_Pass)

cabecera="To"+to+"\n"+"from: "+ gmail_User+"\n"+"Subject: Prueba  \n"

print(cabecera)

mensaje=cabecera+ "\n Este es un mensaje, enviado desde la sala D del curso Intermedio de Pyhton por PROTECO"

smtpserver.sendmail(gmail_User,to,mensaje)

print("Correo enviado!")

#Terminamos la conexion

smtpserver.close()