import socket
import re
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 9868
print('Waiting for connection')

ClientSocket.connect((host, port))

Response = ClientSocket.recv(1024)
Response_utf=Response.decode('utf-8')
print(Response_utf)
while True and not re.search("Merci d'avoir utilisé spotiFREE !$", Response_utf) :
    Input = input('> ')
    ClientSocket.sendall(str.encode(Input))
    Response = ClientSocket.recv(2048)
    Response_utf=Response.decode('utf-8')
    print(Response_utf)

ClientSocket.close()