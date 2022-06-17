
import socket
from _thread import *


ServerSocket = socket.socket()
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
host = '127.0.0.1'
port = 9997
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def connection_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ta requete est : ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(connection_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()