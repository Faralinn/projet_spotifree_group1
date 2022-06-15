import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 9883
print('Waiting for connection')

ClientSocket.connect((host, port))

Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Input = input('> ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()