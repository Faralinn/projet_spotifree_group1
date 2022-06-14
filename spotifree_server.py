#!/usr/bin/env python3
# spotifree
# SERVER
######################
import socket
from _thread import *
import mariadb

###
class gestion_SQL():
    '''
    Classe dediee pour la gestion des requetes SQL 
    => ajouter dans la database
    => chercher dans la database
    => supprimer dans la database
    '''
    def __init__(self):
        '''
        Constructeur. Initialise la connexion avec la database et le curseur
        '''
        self.conn = mariadb.connect(
            user="thurux",
            password="thurux",
            host="127.0.0.1",
            port=3306,
            database="BDPM"
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
    
    def search (self,condition,table):
        '''
        Fonction qui permet de chercher un element dans la base de donnee
        '''
        # condition doit être une chaine de caractère entre "" => ex: condition="Code_CIS=700"
        self.condition=condition
        print("DANS SEARCH",self.condition)
        # table doit être une chaine de caractère entre "" => ex: table="US_citizen"
        self.table=table
        print("DANS SEARCH",self.table)
        self.query=f"SELECT * FROM {table} WHERE {condition};"
        print("DANS SEARCH",self.query)
        self.cur.execute(self.query)
        self.results=self.cur.fetchall()
        return(self.results)
    
    def delete (self,condition,table):
        '''
        Fonction qui permet de supprimer un element de la base de donnee
        '''
        # condition doit être une chaine de caractère entre "" => ex: condition="Code_CIS=700"
        self.condition=condition
        # table doit être une chaine de caractère entre "" => ex: table="US_citizen"
        self.table=table
        self.query=f"DELETE FROM {table} WHERE {condition};"
        self.cur.execute(self.query)


sql=gestion_SQL()
###
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

    def FONCTION_THREAD(self, client_soc):
        '''
        Ce qui se passe sur chaque thread pour chaque client => bcp trop important... !!
        '''
        #client_soc.send(str.encode('Welcome to the Servern'))
        client_soc.send(str.encode('Entrez table et condition pour la recherche SQL'))
        while True:
            data = client_soc.recv(2048)
            data = data.decode('utf-8')
            print("data =",data)
            table, condition=data.split(",",1)
            print("table =", table, "condition=", condition)
            reply= str(sql.search(condition,table))
            # => fonction id/mdp
            # => fonction accueil/choix
            # => redirection vers les commandes
            #reply = 'Server Says: ta requete est : ' + data.decode('utf-8')
            if not data:
                break
            client_soc.sendall(str.encode(reply))
        client_soc.close()

    def accept_connection(self):
        '''
        Fonction qui accepte les connexions socket et attribue un fil (thread) a chaque utilisateur
        '''

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

###
class Spotifriend():
    '''
    Classe qui va nous permettre de manipuler et créer les objets "Spotifriend", à partir du server sql
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
# Main
host="127.0.0.1"
port=9886
server=ServerSocket(host,port)
server.run()


