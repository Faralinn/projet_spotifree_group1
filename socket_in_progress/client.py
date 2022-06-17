import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 9976

print('Waiting for connection')

ClientSocket.connect((host, port))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()