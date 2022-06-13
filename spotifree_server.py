#!/usr/bin/env python3
# spotifree
# SERVER
######################
import socket
import _thread
import mariadb

###
class gestion_SQL():
    '''
    Classe dédiée pour la gestion des requêtes SQL 
    => chercher dans la database
    => ajouter dans la database
    => supprimer dans la database
    '''
    def __init__(self):
        '''
        Constructeur. Initialise la connexion avec la database et le curseur
        '''
        self.conn = mariadb.connect(
            user="server_master",
            password="server_master",
            host="addresseIP_du_docker",
            port=3306,
            database="spotifree"
        )
        self.cur = self.conn.cursor()

    def insertion(self,table,colonnes,data):
        '''
        Fonction qui permet d'ajouter un element dans la base de donnee
        '''
        # table doit être une chaine de caractère entre "" => ex: table="US_citizen"
        self.table=table
        # colonnes doit être une chaine de caractère entre "" => ex: colonnes="nom, age, Etat"
        self.colonnes=colonnes
        # data doit être un tuple où chaque valeur séparée par une virgule est entre '' => ex: data=('john','52','Texas')
        self.data=data
        self.query=f"INSERT INTO {self.table} ({self.colonnes}) VALUES {self.data}"
        self.cur.execute(query)
    
    def search (self,data,table):
        '''
        Fonction qui permet de chercher un element dans la base de donnee
        '''
        self.query="SELECT FROM;"
        self.cur.execute(query)

###
class Socket():
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

        # on bind sur l'hôte et le port donné en paramètre
        print(" Binding to ",self.HOST+":"+str(self.PORT))
        self.soc.bind((self.HOST, self.PORT))

        # on met le server en écoute, pour l'instant limite conventionnelle de 5 requêtes à la fois
        print("Server listening..")
        self.soc.listen(5)

    def broadcast(self,message,connection):
        '''
        Fonction broadcast qui renvoie le message donné en argument sur tous les fils (donc à tous les clients connectés) 
        sauf à celui qui envoie le message
        Si erreur lors de du broadcast, on supprime la connexion défectueuse
        '''
            for client in self.clients:
                if client.clientsocket != connection.clientsocket:
                    try:
                        client.clientsocket.send(message)
                        client.clientsocket.send(connection.user.encode())
                    except:
                        self.remove(connection)


    def send_msg(self,message,connection,client):
        '''
        Fonction send qui envoie le message donné en argument sur un fil (donc à un client connecté)
        Si erreur lors du send, on supprime la connexion défectueuse
        '''
        if client.clientsocket != connection.clientsocket:
            try:
                client.clientsocket.send(message)
                client.clientsocket.send(connection.user.encode())
            except:
                self.remove(connection)

    def accept_connection(self):
        '''
        Fonction qui accepte les connexions socket et attribue un fil (thread) à chaque utilisateur
        TO DO => attribuer id/mdp 
        '''
        self.a=True
        while self.a==True:
            new_client=self.soc.accept()
            if new_client:
                new_client=Client(new_client)
                self.clients.append(new_client)
                _thread.start_new_thread(new_client.run,(self.q,))
                print(" client :",new_client.addr," connected ")

###
class Spotifriend():
    '''
    Classe qui va nous permettre de manipuler et créer les objets "Spotifriend", à partir d'une bdd
    => création d'identifiant/mdp
    => possib d'ajout d'ami
    => possib de supprimer un ami
    => voir liste d'amis
    => droits de read sur les playlists
    '''
    def __init__(self,id,mdp):
        '''
        Fonction d'initialisation pour la classe Spotifriend
        '''
        self.id=id
        self.mdp=mdp

    def creation_id():
        '''
        Fonction pour créer les id et mdp lors d'une première connexion : ajout à la table dédiée
        '''
    def check_id():
        '''
        Fonction pour comparer les inputs id/mdp avec le fichier json
        '''
    def ajout_ami():
        '''
        Fonction
        '''



