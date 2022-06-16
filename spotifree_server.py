#!/usr/bin/env python3
# spotifree
# SERVER
######################
import socket
from _thread import *
import mariadb
import import_spotipy as sp 
from time import sleep

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
            database="spotifree",
            autocommit=True
        )
        self.cur = self.conn.cursor()

    def insertion(self,table,colonnes,data):
        '''
        Fonction qui permet d'ajouter un element dans la base de donnee
        '''
        self.table=table
        self.colonnes=colonnes
        # data doit être un tuple où chaque valeur séparée par une virgule est entre '' => ex: data=('john','52','Texas')
        self.data=data
        self.query=f"INSERT INTO {self.table} ({self.colonnes}) VALUES {self.data};"
        self.cur.execute(self.query)
    
    def search (self,condition,colonnes,table):
        '''
        Fonction qui permet de chercher un element dans la base de donnee
        '''
        self.table=table
        self.colonnes=colonnes
        self.condition=condition
        self.query=f"SELECT DISTINCT {self.colonnes} FROM {self.table} WHERE {self.condition};"
        print(self.query)
        self.cur.execute(self.query)
        self.results=self.cur.fetchall()
        print(self.results)
        chain=""
        for line in self.results:
            for element in line:
                chain+=str(element)+" | "
        return(chain)
        # return(self.results)
    
    def delete (self,condition,table):
        '''
        Fonction qui permet de supprimer un element de la base de donnee
        '''
        self.condition=condition
        self.table=table
        self.query=f"DELETE FROM {table} WHERE {condition};"
        self.cur.execute(self.query)


sql=gestion_SQL()
###
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
        self.colonnes="pseudo"
        self.table="identifiants"
        self.condition=self.colonnes+" LIKE \""+self.username+"\""
        print(self.condition)
        self.usernames=sql.search(self.condition,self.colonnes,self.table)
        #self.query=f"SELECT DISTINCT {self.colonnes} FROM {self.table} WHERE {self.condition};"
        check=False
        if self.username in self.usernames :
            check=True
        return check
        #fonction vérifiant si le mot de passe donné est correct
    def check_passwd(self,username,passwd) :
        
        self.username=username
        self.colonnes="mot_de_pass"
        self.table="identifiants"
        self.condition="pseudo LIKE \""+self.username+"\""
        self.passwd=passwd+" | "
        self.password=sql.search(self.condition,self.colonnes,self.table)
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
            self.colonnes="pseudo, mot_de_pass"
            self.table="identifiants"
            self.data=f"(\'{self.username}\',\'{self.passwd}\')"
            sql.insertion(self.table,self.colonnes,self.data)



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
            while True:
                self.fonction_menu(self.client_soc)
        self.send_msg(self.client_soc,"Merci d'avoir utilisé spotiFREE !")


    def recherche(self,by_what,client_soc):
        '''
        Fonction qui demande au client via socket le nom de l'artiste, album ou musique pour executer la requete sql
        et renvoyer le resultat de cette requete au client via socket
        '''
        self.by_what=by_what
        self.client_soc=client_soc
        self.table="listing"
        if self.by_what == "by_artist":
            self.colonnes="*"
            self.msg="Entrez le nom de l'artiste : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="artist"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            print(self.reply)
            self.send_msg(self.client_soc,self.reply)
            # self.menu_trouve()
        elif self.by_what == "by_album":
            self.colonnes="*"
            self.msg="Entrez le nom de l'album : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="album"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            self.send_msg(self.client_soc,self.reply)
            # self.menu_trouve()
        elif self.by_what == "by_music":
            self.colonnes="*"
            self.msg="Entrez le nom du titre : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="title"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            self.send_msg(self.client_soc,self.reply)
            # if reply != "":
            #     self.menu_trouve()
        else:
            self.msg="Erreur dans la fonction recherche"
            print(msg)
            self.send_msg(msg)
            return(False)

    def fonction_menu(self,client_soc):
        '''
        Fonction qui affiche un menu au client via socket, pour choisir les actions
        que le client souhaite realiser
        TO DO => envoyer le pseudo en parametre de la fonction menu
        pour le moment pseudo arbitraire = arthur
        '''
        self.client_soc=client_soc
        self.menu=" 1/ Faire une recherche\n 2/ Gestion des playlists\n 3/ Mes ami.es\n "
        self.send_msg(self.client_soc,self.menu)
        self.data = self.receive_msg(self.client_soc)
        if self.data == "1":
            # recherche=True
            self.menu=" RECHERCHE :\n 1/ PAR ARTISTE\n 2/ PAR ALBUM\n 3/ PAR MUSIQUE\n "
            self.send_msg(self.client_soc,self.menu)
            self.data = self.receive_msg(self.client_soc)
            if self.data == "1":
                self.by_what="by_artist"
                self.recherche(self.by_what,self.client_soc)
            elif self.data == "2":
                self.by_what="by_album"
                self.recherche(self.by_what,self.client_soc)
            elif self.data == "3":
                self.by_what="by_music"
                self.recherche(self.by_what,self.client_soc)
            else:
                self.msg="Erreur dans le choix"
                self.client_soc.send(self.client_soc,self.msg)
                return(False)
        elif self.data == "2":
            # playlist=True
            self.condition="pseudo"+" LIKE \"%"+"arthur"+"%\""
            self.colonnes="titre_playlist"
            self.table="playlist"
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            self.send_msg(self.client_soc,self.reply)
            self.menu=" PLAYLIST :\n 1/ PAR ARTISTE\n 2/ PAR ALBUM\n 3/ PAR MUSIQUE\n "
            self.send_msg(self.client_soc,self.menu)
            self.data = self.receive_msg(self.client_soc)

        else:
            pass

    def FONCTION_THREAD(self, client_soc):
        '''
        Ce qui se passe sur chaque thread pour chaque client => equivalent de notre main !!
        '''
        self.client_soc=client_soc
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
port=9868
server=ServerSocket(host,port)
server.run()


