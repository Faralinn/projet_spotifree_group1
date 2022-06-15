import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 9868
print('Waiting for connection')

ClientSocket.connect((host, port))

Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Input = input('> ')
    ClientSocket.sendall(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))

ClientSocket.close()