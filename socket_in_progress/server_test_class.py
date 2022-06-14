
import socket
from _thread import *

host = '127.0.0.1'
port = 9976

class ServerSocket():
    def __init__(self,host,port):
        '''
        Fonction d'initialisation du socket server
        => on donne l'hôte et le port en paramètre
        '''
        # création du socket et de la liste des clients
        self.soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.HOST=host
        self.PORT=port
        self.clients=[]
        self.ThreadCount = 0

        self.soc.bind((self.HOST, self.PORT))

# on met le server en écoute, pour l'instant limite conventionnelle de 5 requêtes à la fois
        print("Server listening...")
        self.soc.listen(5)
        print("----MARQUE 1 ----\n")

    def FONCTION_THREAD(self, client_soc):
        print("----MARQUE 3 ----\n")
        client_soc.send(str.encode('Welcome to the Servern'))
        while True:
            data = client_soc.recv(2048)
            reply = 'Server Says: ta requete est : ' + data.decode('utf-8')
            if not data:
                break
            client_soc.sendall(str.encode(reply))
        client_soc.close()

    def accept_connection(self):
        '''
    Fonction qui accepte les connexions socket et attribue un fil (thread) à chaque utilisateur
    TO DO => attribuer id/mdp 
        '''
        print("----MARQUE 2 ----\n")
        self.a=True
        while self.a==True:
            new_client, address=self.soc.accept()
            if new_client:
                self.clients.append(new_client)
                
                start_new_thread(self.FONCTION_THREAD,(new_client, ))
                print(" client :",address," connected ")
                self.ThreadCount += 1
                print('Thread Number: ' + str(self.ThreadCount))


    def run(self) :
        self.accept_connection()
        print("----MARQUE 4 ----\n")

server=ServerSocket(host,port)
server.run()