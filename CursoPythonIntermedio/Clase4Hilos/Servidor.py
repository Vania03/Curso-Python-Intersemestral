#Servidor

import socket
recvIp=input("Ingresa la IP a la que te quieres conectar: ")
ss=socket.socket()
ss.bind((recvIp,9001))
ss.listen(1)

conn,addr=ss.accept()
print("Iniciando servidor!!")
print("Cliente conectado desde: ",addr[0],": ",addr[1])

while True:
	recibido=conn.recv(5000).decode()
	if recibido=="adios":
		break
	print("Cliente dice: ",recibido)
	conn.send(input("Ingresa tu mensaje: ").encode())

print("Se ha terminado la conexion")
ss.close()