# echo-client.py
import socket
import _thread


def afficher(s):
    while True:
        data = s.recv(1024)
        data=data.decode()
        print("\033[0;31m Received ",data,"\033[0;0m")

def envoyer(s):
    while True:
        print("\033[0;35m")
        msg=input("> ")
        print("\33[0;0m")
        s.send(msg.encode())



HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8083  # The port used by the server

threads=[]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    i=0
    while True:
        if i<1:
            threads.append(_thread.start_new_thread(afficher,(s,)))
            threads.append(_thread.start_new_thread(envoyer,(s,)))
            i+=1
            print(threads)