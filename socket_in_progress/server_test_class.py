#!/usr/bin/env python3
# spotifree
# SERVER
######################
import socket
from _thread import *
from time import sleep
import mariadb
import import_spotipy as sp 


###
class gestion_SQL():
    '''
    Classe dediee pour la gestion des requetes SQL 
    => ajouter dans la database
    => chercher dans la database
    => supprimer dans la database
    '''

    # Constructeur. Initialise la connexion avec la database et le curseur
    def __init__(self):
        self.conn = mariadb.connect(
            user="soufian",
            password="soufian",
            host="127.0.0.1",
            port=3306,
            database="spotifree"
        )
        self.cur = self.conn.cursor()

    #Fonction permettant d'ajouter un element dans la base de donnee
    def insertion(self,table,colonnes,data):
        self.table=table
        self.colonnes=colonnes
        # data doit être un tuple où chaque valeur séparée par une virgule est entre '' => ex: data=('john','52','Texas')
        self.data=data
        print(sql.search("select pseudo from identifiants;"))
        self.query=f"INSERT INTO {self.table} ({self.colonnes}) VALUES {self.data};"
        
        print(self.query)
        self.cur.execute(self.query)
        print(sql.search("select pseudo from identifiants;"))

    
    #Fonction permettant de chercher un element dans la base de donnee
    def search (self,query):
        self.query=query
        self.cur.execute(self.query)
        self.results=self.cur.fetchall()
        chain=""
        for line in self.results:
            for element in line:
                chain+=str(element)+" | "
        return(chain)
    
    #Fonction permettant de supprimer un element de la base de donnee
    def delete (self,condition,table):
        self.condition=condition
        self.table=table
        self.query=f"DELETE FROM {table} WHERE {condition};"
        self.cur.execute(self.query)


sql=gestion_SQL()

class ServerSocket():

    def __init__(self,host,port):
        '''
        Fonction d'initialisation du socket server
        => on donne l'hote et le port en parametre
        '''
        # création du socket et de la liste des clients
        self.soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.soc.settimeout(0)
        self.HOST=host
        self.PORT=port
        self.clients=[]
        self.ThreadCount = 0
        self.soc.bind((self.HOST, self.PORT))
        # on met le server en écoute, pour l'instant limite conventionnelle de 5 requêtes à la fois
        print("Server listening...")
        self.soc.listen(5)

    def send_msg(self,client_soc,msg) :
        '''
        Fonction pour envoyer des donnees au client via socket
        '''
        self.msg=msg
        self.client_soc=client_soc
        self.client_soc.sendall(str.encode(self.msg))
        
    def receive_msg(self,client_soc) :
        '''
        Fonction pour recevoir les data du client via socket
        '''
        self.client_soc=client_soc
        self.data = self.client_soc.recv(2048)
        self.data = self.data.decode('utf-8')
        return(self.data)

    #fonction vérifiant si le pseudo existe déjà ans la base de donnée
    def check_username(self,username) :
        self.username=username
        self.usernames=sql.search("select pseudo from identifiants where pseudo LIKE \""+self.username+"\";")
        check=False
        if self.username in self.usernames :
            check=True
        return check
        #fonction vérifiant si le mot de passe donné est correct
    def check_passwd(self,username,passwd) :
        
        self.username=username
        self.passwd=passwd+" | "
        self.password=sql.search("select mot_de_pass from identifiants where pseudo LIKE \""+self.username+"\";")
        print("  passwd : ",self.passwd)
        print("password : ",self.password)
        check=False
        if self.passwd == self.password :
            check=True
        return check

    #fonction régissant la connexion de l'utilisateur. Cette fonction est appelée par la fonction login.
    #Si la connexion est réussie, lancement de la fonction principale du script.
    def connexion(self,client_soc):
        self.client_soc=client_soc
        self.next_step=""
        self.send_msg(self.client_soc,"Nom d'utilisateur : ")
        self.username = self.receive_msg(self.client_soc)
        self.check=self.check_username(self.username)
        if not self.check :
            self.msg="Le compte "+self.username+" n'existe pas ! Etes vous sur d'avoir un compte ?\n1- Réessayer\n2- Retour au menu principal\nChoisissez une option : "
            self.send_msg(self.client_soc,self.msg)
            self.sign_in = self.receive_msg(self.client_soc)
            if self.sign_in == "1" :
                self.next_step="connexion"
            elif self.sign_in == "2" :
                self.next_step="menu"
            else :
                self.send_msg(self.client_soc,"Option non reconnue. Retour au menu principal.")
                self.next_step="menu"
        else :
            self.send_msg(self.client_soc,"Mot de passe : ")
            self.passwd = self.receive_msg(self.client_soc)
            self.check=self.check_passwd(self.username, self.passwd)
            self.tries=1
            while not self.check and self.tries<5 and self.next_step != "menu":
                self.msg="Mot de passe incorrect !\n--------------------------------------------------\n1- Réessayer\n2- Retour au menu principal\nChoisissez une option : "
                self.send_msg(self.client_soc,self.msg)
                self.sign_in = self.receive_msg(self.client_soc)
                if self.sign_in == "1" :
                    self.send_msg(self.client_soc,"Mot de passe : ")
                    self.passwd = self.receive_msg(self.client_soc)
                    self.check=self.check_passwd(self.username, self.passwd)
                    self.tries+=1
                elif self.sign_in == "2" :
                    self.next_step="menu"
                else : 
                    self.send_msg(self.client_soc,"Option non reconnue.\n")
                    
            
            if self.check :
                self.msg="Connexion réussie. Bienvenue, "+self.username+" !\n"
                self.send_msg(self.client_soc,self.msg)
                self.next_step="spotiFREE"
            elif self.next_step=="menu" :
                pass
            else :
                self.msg="Mot de passe incorrect. Nombre de tentatives autorisées dépassé. Déconnexion. \n"
                self.send_msg(self.client_soc,self.msg)
                self.next_step="exit"
        return(self.next_step)

    def creation(self, client_soc):
        self.client_soc=client_soc
        self.sign_up=""
        self.next_step="menu"
        self.send_msg(self.client_soc,"Choisissez un nom d'utilisateur : ")
        self.username = self.receive_msg(self.client_soc)
        self.check=self.check_username(self.username)
        while self.check :
            self.msg="Le compte "+self.username+" existe déjà.\n"
            self.send_msg(self.client_soc,self.msg)
            self.msg="1- Réessayer\n2- Retour au menu principal\nChoisissez une option : "
            self.send_msg(self.client_soc,self.msg)
            self.sign_up = self.receive_msg(self.client_soc)
            if self.sign_up == "1" :
                self.send_msg(self.client_soc,"Choisissez un nom d'utilisateur : ")
                self.username = self.receive_msg(self.client_soc)
                self.check=self.check_username(self.username)
            elif self.sign_up == "2" :
                self.check=False
            else :
                self.send_msg(self.client_soc,"Option non reconnue.\n")
        if self.sign_up != "2" :
            self.send_msg(self.client_soc,"Veuillez choisir un mot de passe : ")
            self.passwd = self.receive_msg(self.client_soc)
            self.send_msg(self.client_soc,"Veuillez confirmer le mot de passe : ")
            self.passwd2 = self.receive_msg(self.client_soc)
            while self.passwd != self.passwd2 :
                self.send_msg(self.client_soc,"Les mots de passe ne sont pas identiques.\n")
                self.send_msg(self.client_soc,"Veuillez choisir un mot de passe : ")
                self.passwd = self.receive_msg(self.client_soc)
                self.send_msg(self.client_soc,"Veuillez confirmer le mot de passe : ")
                self.passwd2 = self.receive_msg(self.client_soc)
            self.msg="Le compte "+self.username+" a bien été créé.\n"
            self.send_msg(self.client_soc,self.msg)
            #ici stocker le compte username,passwd
            print(f"(\'{self.username}\',\'{self.passwd}\')")
            sql.insertion("identifiants","pseudo,mot_de_pass",f"(\'{self.username}\',\'{self.passwd}\')")



    def login(self,client_soc) :
        self.client_soc=client_soc
        self.next_step="menu"
        self.send_msg(self.client_soc,"Spotifree, la musique au bout du tunnel !\nAppuyez sur Entree pour continuer...\n")
        while self.next_step=="menu" or self.next_step == "connexion":  
            if self.next_step == "connexion" :
                self.next_step=self.connexion(self.client_soc)
            else :
                self.send_msg(self.client_soc,"-----------------------------------------\nMenu principal.\n1- Connexion\n2- Créer un compte\nChoisissez une option : ")
                self.sign = self.receive_msg(self.client_soc)
                if self.sign == "1" :
                    self.next_step=self.connexion(self.client_soc)
                elif self.sign == "2" :
                    self.creation(self.client_soc)
                else :
                    self.send_msg(self.client_soc,"Option non reconnue.\n")
        if self.next_step == "spotiFREE":
            print("ici la fonction spotiFREE.\n")
            self.send_msg(self.client_soc,"ici la fonction spotiFREE.\n")
            #fonction ici
        self.send_msg(self.client_soc,"Merci d'avoir utilisé spotiFREE !")


    def FONCTION_THREAD(self, client_soc):
        '''
        Ce qui se passe sur chaque thread pour chaque client => equivalent de notre main !!
        '''
        self.client_soc=client_soc
        # fonction login
        self.login(self.client_soc)                          
        self.client_soc.close()

    def accept_connection(self):
        '''
        Fonction qui accepte les connexions socket et attribue un fil (thread) a chaque utilisateur
        '''
        new_client=None
        address=None
        self.a=True
        while self.a==True:
            try:
                new_client, address=self.soc.accept()
            except:
                sleep(0.5)
            if new_client:
                self.clients.append(new_client)
                
                start_new_thread(self.FONCTION_THREAD,(new_client, ))
                print(" client :",address," connected ")
                self.ThreadCount += 1
                print('Thread Number: ' + str(self.ThreadCount))
            new_client=None

    def run(self) :
        self.accept_connection()




# Main
host="127.0.0.1"
port=9867
server=ServerSocket(host,port)
server.run()


