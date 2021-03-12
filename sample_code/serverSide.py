# Test code for building a basic chatroom
# sample code pulled from https://www.tutorialspoint.com/simple-chat-room-using-python

import time, socket, sys
print('Setup Server...')
time.sleep(1)

#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))

#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
while True:
	message = input('Me > ')
	if message == '[bye]':
		message = 'Good Night...'
		connection.send(message.encode())
		print("\n")
		break
	connection.send(message.encode())
	message = connection.recv(1024)
	message = message.decode()
	print(client_name, '>', message)
