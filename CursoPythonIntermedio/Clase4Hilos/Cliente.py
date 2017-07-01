#Cliente
#
import socket
#Definimos el objeto
s=socket.socket()
s.connect(("localhost",9000))

while True:
#mandamos el mensaje
	mensaje=input("Ingresa tu mensaje: ")
	s.send(mensaje.encode())
	if mensaje=="adios":
		break
	respuesta=s.recv(1024).decode()
	print("Respuesta del servidor: ",respuesta)

print("Finaliza la conexion")
s.closed()