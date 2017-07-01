#-*-coding:utf-8-*
#Simple Mail Transfer Protocol
import smtplib
#Esto es muy importante, porque son los datos del que envia
elQueEnvia="cursopython.proteco@gmail.com"
contra="python.isCool"
#El que recibe, o al que enviamos correo
elQueRecibe="yesii.fresita.aguirre@gmail.com"

#El mensaje
mensaje="""From: cursoPython <cursopython.proteco@gmail.com>
To: <yesii.fresita.aguirre@gmail.com>
MIME-Version:1.0
Content-type: text/html

Subject: Hola mejor amiga Yesii :D

<div style="font-family:'Pacifico',cursive; background:#CBAEAE">
<center>
<h1> Este es un mensaje de tu mejor amiga : <span style='color:red'> Vania Martinez</span></h1>
<p style="color:gray">El correo fue enviado desde la sala B </p>
</center>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</div>
"""

try:
	smtpObjeto=smtplib.SMTP("smtp.gmail.com",587)
	smtpObjeto.ehlo()#Saludamos con el metodo Ehlo
	smtpObjeto.starttls()
	smtpObjeto.ehlo #Este es el atributo ehlo
	#LOGIN (CORREO,CONTRASEÑA)
	smtpObjeto.login(elQueEnvia,contra)
	smtpObjeto.sendmail(elQueEnvia,elQueRecibe,mensaje)
	print("\n\n\t\tFELICIDADES, se ha enviado tu correo!!! :D ")
except Exception as e:
	print("Error,no pude enviar tu mensaje, revisa tu programa!! :C")
	print(e)