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
            user="spoti",
            password="spotipass",
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
        self.cur.execute(self.query)
        self.results=self.cur.fetchall()
        chain=""
        for line in self.results:
            chain+="\n"
            for element in line:
                chain+=str(element)+" | "
        return(chain)
        # return(self.results)
    # def update (): 
    
    def delete (self,condition,table):
        '''
        Fonction qui permet de supprimer un element de la base de donnee
        '''
        self.condition=condition
        self.table=table
        self.query=f"DELETE FROM {table} WHERE {condition};"
        self.cur.execute(self.query)
        
#création d'une instance de la classe gestion_SQL pour interragir avec la base de données
sql=gestion_SQL()
###

class ServerSocket():  
    '''
    Classe dedié"e pour la création et l'utilisation des sockets dans les différentes fonctions du programme.
    Ces fonctions sont codés en tant que méthode de cette classe.
    '''
    # Fonctions de base du socket
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

    # Blocs de fonctions gérant la création et l'identification des utilisateurs

    def check_username(self,username) :
        '''
        Fonction vérifiant l'existence d'un utilisateur
        '''
        self.username=username
        self.colonnes="pseudo"
        self.table="identifiants"
        self.condition=self.colonnes+" LIKE \""+self.username+"\""
        self.usernames=sql.search(self.condition,self.colonnes,self.table)
        check=False
        if self.username in self.usernames :
            check=True
        return check

    def check_passwd(self,username,passwd) :
        '''
        Fonction vérifiant si le mot de passe entré pour un utilisateur donné est correct
        '''
        self.username=username
        self.colonnes="mot_de_pass"
        self.table="identifiants"
        self.condition="pseudo LIKE \""+self.username+"\""
        self.passwd="\n"+passwd+" | "
        self.password=sql.search(self.condition,self.colonnes,self.table)
        check=False
        if self.passwd == self.password :
            check=True
        return check

    def connexion(self,client_soc):
        '''
        Fonction regissant la connexion de l'utilisateur. Cette fonction est appelée par la fonction login.
        Si la connexion est réussie, lancement de la fonction principale du script.
        '''
        self.client_soc=client_soc
        self.next_step=""
        self.send_msg(self.client_soc,"Nom d'utilisateur : ")
        self.username = self.receive_msg(self.client_soc)
        #on vérifie si l'utilisateur existe
        self.check=self.check_username(self.username)
        if not self.check :
             #s'il n'existe pas, on propose à l'utilisateur de réessayer ou de retourner au menu du login
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
            #si l'utilisateur existe, on demande le mot de passe et on le teste.
            self.send_msg(self.client_soc,"Mot de passe : ")
            self.passwd = self.receive_msg(self.client_soc)
            self.check=self.check_passwd(self.username, self.passwd)
            self.tries=1
            #si le mot de passe est faux, on le redemande jusqu'à 5 fois puis on arrête la connexion.
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
                    
            #si le mot de passe est bon, on affiche de message d'accueil et le menu principal.
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
        #next_step permet de diriger le programme vers la prochaine étape en fonction du déroulement de la connexion 
        # (menu login, exit ou spotifree pour accéder à l'application)
        return(self.next_step)

    def creation(self, client_soc):
        '''
        Fonction gérant la création des comptes utilisateur. Cette fonction est appelée par la fonction login.
        Si la création est réussie, ajout du compte dans la BDD et redirection vers l'interface de connexion.
        '''
        self.client_soc=client_soc
        self.sign_up=""
        self.next_step="menu"
        self.send_msg(self.client_soc,"Choisissez un nom d'utilisateur : ")
        self.username = self.receive_msg(self.client_soc)
        #on vérifie si l'utilisateur n'est pas déjà dans la BDD
        self.check=self.check_username(self.username)
        #sinon on redemande un nom d'utilisateur, en laissant l'option de retourner à l'interface de connexion
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
            #si l'utilisateur veut retourner à l'écran de connexion, on sort de la boucle.
            elif self.sign_up == "2" :
                self.check=False
            else :
                self.send_msg(self.client_soc,"Option non reconnue.\n")
        #on entre dans cette boucle if si l'utilisateur a bien donné un nom valide
        #on lui demande un mot de passe qu'il devra confirmer une seconde fois.
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
            #on stocke le compte (username,passwd) dans la BDD
            self.colonnes="pseudo, mot_de_pass"
            self.table="identifiants"
            self.data=f"(\'{self.username}\',\'{self.passwd}\')"
            sql.insertion(self.table,self.colonnes,self.data)

    def login(self,client_soc) :
        '''
        Fonction gérant le processus d'identification. Cette fonction appelle les fonctions décrites précedemment.
        On avance dans le processus en fonction de la valeur de la variable "next_step", 
        qui est modifiée par les retours des fonctions de connexion et de création de compte.
        '''
        self.client_soc=client_soc
        #on initie next_step à menu pour accéder au menu du login
        self.next_step="menu"
        self.send_msg(self.client_soc,"Spotifree, la musique au bout du tunnel !\nAppuyez sur Entree pour continuer...\n")
        #boucle while principale du menu redirigeant vers les fonctions appropriées.
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
        #si la connexion est validée, on lance la fonction du menu principal et l'utilisateur peut accéder aux différents services.
        if self.next_step == "spotiFREE":
            while True:
                self.fonction_menu(self.client_soc,self.username)
        #si next_step a une autre valeur que menu, connexion ou spotiFREE, on sort du programme.
        self.send_msg(self.client_soc,"Merci d'avoir utilisé spotiFREE !")

    # Gestion database
    def recherche_spotipy(self,client_soc):
        '''
        Fonction qui demande au client via socket le nom de l'artiste, album ou musique pour executer la requete sql
        et renvoyer le resultat de cette requete au client via socket
        utilisation de la fonction sp.getDiscography() programmée dans le fichier import_spotipy.py
        '''
        self.client_soc=client_soc
        self.table="listing"
        self.menu=" RECHERCHE :\n 1/ PAR ARTISTE\n 2/ PAR ALBUM\n 3/ PAR MUSIQUE\n 4/ RETOUR\n"
        self.send_msg(self.client_soc,self.menu)
        self.data = self.receive_msg(self.client_soc)
        #on redirige vers l'option choisie
        if self.data == "1":
            self.colonnes="*"
            self.msg="Entrez le nom de l'artiste : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="artist"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            print(self.reply)
            self.send_msg(self.client_soc,self.reply)
        elif self.data == "2":
            self.colonnes="*"
            self.msg="Entrez le nom de l'album : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="album"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            self.send_msg(self.client_soc,self.reply)
        elif self.data == "3":
            self.colonnes="*"
            self.msg="Entrez le nom du titre : "
            self.send_msg(self.client_soc, self.msg)
            self.input = self.receive_msg(self.client_soc)
            self.condition="title"+" LIKE \"%"+self.input+"%\""
            sp.getDiscography(self.input)
            self.reply= str(sql.search(self.condition,self.colonnes,self.table))
            self.send_msg(self.client_soc,self.reply)
        elif self.data == "4":
            fonction_menu(self.client_soc)
        else:
            self.msg="Erreur dans le choix"
            self.client_soc.send(self.client_soc,self.msg)
            return(False)

    #bloc de fonctions gérant le système de playlists
    #TO DO : - option 2 à implémenter "partager une playlist"
    #        - option 4 à implémenter "supprimer une playlist" 
    def afficher_playlist(self,client_soc,username):
        '''
        fonction permettant d'afficher les titres d'une playlist
        '''
        self.client_soc=client_soc
        self.username=username
        self.menu="De quelle playlist voulez-vous afficher les titres ?\n"
        self.send_msg(self.client_soc,self.menu)
        self.data = self.receive_msg(self.client_soc)
        self.condition="titre_playlist LIKE \"%"+self.data+"%\""
        print("dans afficher_playlist ", self.condition)
        self.colonnes="artist,musique"
        self.table=self.data
        self.reply="Voici les titres de "+self.data+": \n"+str(sql.search(self.condition,self.colonnes,self.table))+"\n\n"
        self.send_msg(self.client_soc,self.reply)

    def partager_playlist(self,client_soc,username):
        '''
        fonction permettant de partager une playlist à un de ses amis
        non fonctionnelle en l'état
        '''
        self.client_soc=client_soc
        self.username=username
        self.menu="Quelle playlist voulez-vous partager ?\n"
        self.send_msg(self.client_soc,self.menu)
        self.playlist_to_share = self.receive_msg(self.client_soc)
        self.menu="Avec quel.le ami.e voulez-vous partager "+self.playlist_to_share+" ?\n"
        self.send_msg(self.client_soc,self.menu)
        self.friend_to_share_with = self.receive_msg(self.client_soc)
        self.colonnes="utilisateurs"
        self.table="playlists"
        self.data=f"(\'{self.friend_to_share_with}\',\'{self.passwd}\')"
        #sql.insertion(self.table,self.colonnes,self.data)

    def creation_playlist(self,client_soc,username):
        '''
        fonction permettant de créer une playlist
        '''
        self.client_soc=client_soc
        self.username=username
        self.msg="Choisissez un nom pour la playlist : "
        self.send_msg(self.client_soc,self.msg)
        self.playlist_name=self.receive_msg(self.client_soc)
        query=f"CREATE TABLE {self.playlist_name} (titre_playlist VARCHAR(30) PRIMARY KEY,artist TEXT,musique TEXT,FOREIGN KEY (titre_playlist) REFERENCES playlists (titre_playlist)) ENGINE = InnoDB;"
        sql.cur.execute(query)
        
    def gestion_playlist(self,client_soc,username):
        '''
        fonction principale implémentant le menu et les options disponibles pour gérer ses playlists
        '''
        self.username=username
        self.condition="utilisateurs"+" LIKE \"%"+self.username+"%\""
        self.colonnes="titre_playlist"
        self.table="playlists"
        self.reply="#### LISTE DES PLAYLISTS ####\n"+str(sql.search(self.condition,self.colonnes,self.table))+"\n"
        self.send_msg(self.client_soc,self.reply)
        self.menu="\n 1/ AFFICHER LES TITRES\n 2/ PARTAGER AVEC UN.E AMI.E\n 3/ CREER NOUVELLE PLAYLIST\n 4/ SUPPRIMER UNE PLAYLIST\n 5/ RETOUR\n"
        self.send_msg(self.client_soc,self.menu)
        self.data = self.receive_msg(self.client_soc)
        if self.data == "1":
            self.afficher_playlist(self.client_soc,self.username)
        elif self.data == "2":
            self.partager_playlist(self.client_soc,self.username)
        elif self.data == "3":
            self.creation_playlist(self.client_soc,self.username)
        elif self.data == "4":
            pass
        elif self.data == "5":
            fonction_menu(self.client_soc)
        else:
            self.msg="Erreur dans le choix"
            self.client_soc.send(self.client_soc,self.msg)
            return(False)

    #bloc de fonctions gérant le système d'ami
    #TO DO : correction de bugs dans la suppression et l'ajout d'amis dans la BDD

    def add_friends(self,client_soc,username,friends) :
        '''
        fonction ajoutant un autre utilisateur à sa liste d'amis
        '''
        self.client_soc=client_soc
        self.user=username
        self.friends=friends
        
        self.menu="Veuillez entrer le nom d'un ami : "
        self.send_msg(self.client_soc,self.menu)
        self.friendname = self.receive_msg(self.client_soc)

        #on vérifie si l'ami à ajouter existe et s'il n'est pas déjà dans la lsite d'ami
        if not self.check_username(self.friendname) :
            self.send_msg(self.client_soc,"Cet utilisateur n'existe pas !\n")
        elif (f'{self.friendname}',) in self.friends :
            self.msg="Vous êtes déjà amis avec "+self.friendname+" !\n"
            self.send_msg(self.client_soc,self.msg)
        else :
            self.data=f"(\'{self.user}\',\'{self.friendname}\')"
            sql.insertion("spotifriends","pseudo,amis",self.data)
            self.msg=self.friendname+" ajouté à la liste d'ami !\n"
            self.send_msg(self.client_soc,self.msg)

    def delete_friends(self,client_soc,username,friends) :
        '''
        fonction supprimant un utilisateur de sa liste d'amis
        '''
        self.client_soc=client_soc
        self.user=username
        self.friends=friends
        
        self.menu="Veuillez entrer le nom d'un ami : "
        self.send_msg(self.client_soc,self.menu)
        self.friendname = self.receive_msg(self.client_soc)
        print("friend : ",(f'{self.friendname}',))
        print("friends : ",self.friends)

        #on vérifie si l'ami à retirer est bien dans la lsite d'ami
        if not (f'{self.friendname}',) in self.friends :
            self.msg="Cet utilisateur n'est pas dans votre liste d'ami.\n"
            self.send_msg(self.client_soc,self.msg)
        else :
            self.data=f"pseudo LIKE \'{self.user}\' and amis LIKE \'{self.friendname}\'"
            sql.delete(self.data,"spotifriends")
            self.msg=self.friendname+" supprimé de la liste d'ami.\n"
            self.send_msg(self.client_soc,self.msg)

    def list_friends(self,username) :
        '''
        fonction permettant de lister les amis d'un utilisateur
        '''
        self.username=username
        sql.cur.execute("SELECT amis FROM spotifriends WHERE pseudo LIKE \'"+self.username+"\'")
        self.friends=sql.cur.fetchall()
        return(self.friends)

    def spotifriends(self,client_soc,username):
        '''
        fonction principale implémentant le menu et les options disponibles pour gérer sa liste d'amis.
        '''
        self.client_soc=client_soc
        self.username=username
        self.exit="0"
        #boucle principale. Tant que l'utilisateur ne demande pas à retourner au menu principal, on lui repropose le menu spotifreinds.
        while self.exit == "0":
            #on commence chaque boucle par afficher sa liste d'amis et le menu des options disponibles.
            self.friends=self.list_friends(self.username)
            if self.friends == [] :
                self.msg="Ajoutez des amis pour partager vos playlists !\n"
                self.send_msg(self.client_soc,self.msg)
            else :
                self.msg="Liste de vos amis : "
                for ami in self.friends :
                    self.msg=self.msg+ami[0]+" | "
                self.msg=self.msg+"\n"
                self.send_msg(self.client_soc,self.msg)

            self.menu="1/ Ajouter un ami\n2/ Supprimer un ami\n3/ Retour Menu\n"
            self.send_msg(self.client_soc,self.menu)
            self.choix = self.receive_msg(self.client_soc)

            if self.choix == "1":
                self.add_friends(self.client_soc,self.username,self.friends)
            elif self.choix == "2":
                self.delete_friends(self.client_soc,self.username,self.friends)
            elif self.choix == "3":
                self.exit= "1"
            else :
                pass

            
    ##########################
    def fonction_menu(self,client_soc,username):
        '''
        Fonction qui affiche un menu au client via socket, pour choisir les actions
        que le client souhaite realiser
        Cette fonction est appelée dans la fonction login après l'identification de l'utilisateur.
        '''
        self.username=username
        self.client_soc=client_soc
        self.menu=" 1/ Faire une recherche\n 2/ Gestion des playlists\n 3/ Mes ami.es\n "
        self.send_msg(self.client_soc,self.menu)
        self.data = self.receive_msg(self.client_soc)
        if self.data == "1":
            self.recherche_spotipy(self.client_soc)
        elif self.data == "2":
            self.gestion_playlist(self.client_soc,self.username)
        elif self.data == "3":
            self.spotifriends(self.client_soc,self.username)
        else:
            pass
    ##########################

    # Fonctions de connection et de lancement, génération des threads
    def FONCTION_THREAD(self, client_soc):
        '''
        Cette fonction est appelée à chaque lancement de thread, pour chaque client qui se connecte au serveur.
        Elle lance la fonction login qui permet à l'utilisateur de s'identifier afin d'accéder à Spotifree.
        '''
        self.client_soc=client_soc
        self.login(self.client_soc)                          
        self.client_soc.close()

    def accept_connection(self):
        '''
        Fonction qui accepte les connexions socket et attribue un fil (thread) a chaque utilisateur.
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
port=9868
server=ServerSocket(host,port)
server.run()


