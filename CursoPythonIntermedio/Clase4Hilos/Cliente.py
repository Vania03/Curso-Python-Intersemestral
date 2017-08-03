#Cliente
#
import socket
#Definimos el objeto
recvIP=input("Ingresa la IP a la que te quieres conectar: ")
s=socket.socket()
s.connect((recvIP,9001))

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