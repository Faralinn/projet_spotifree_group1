
                       __  .__  _____.__               
  ____________   _____/  |_|__|/ ____\__| ____   ____  
 /  ___/\____ \ /  _ \   __\  \   __\|  |/ __ \_/ __ \ 
 \___ \ |  |_> >  <_> )  | |  ||  |  |  \  ___/\  ___/ 
/____  >|   __/ \____/|__| |__||__|  |__|\___  >\___  >
     \/ |__|                                 \/     \/ 


###### creation d 'une application spotifee#####

#### auteurs  By _**Arthur GARRIGUE**_**_Cannelle DUGUET_**_**Soufian SAHLI**_**_Ayet Imen BERRADJ**_**Camille BARILLET **_
""" creation de deux teams :
- team Python : Arthur GARRIGUE, Soufian SAHLI, Cannelle DUGUET
- team SQL SQL Lite/SQL : Ayet Imen BERRADJ, Camille BARILLET

## Requirements :
"""" 
- serveur client
- sockets 
- gestions de base de données

**spotipy** est une application qui introduit la performance et la simplicité de l'utilisation de concepts informatiques comme les sockets en python, les bases des requetes SQL et du serveur MariaDB avec une 
            intégration continue sous la forme de docker
            
     #spotipy : permet d'effectuer des recherches dans l'API Spotify via python ; cette application pour son fonctionnement et en fonction du besoin neccessite l'installation  de plusieurs modules python ( pandas,....) . Au début du script python on fera appelle à ces modules par la fonction import +nom du module (ex import spotipy pour spotipy).


## Fonctionnement de l'application    
schema sur blackboard

## work environement
     # Utilisation de python sur Windows  ou sur Linux  
     # Possibilité de faire le travail sur machine Virtuelle Vm ou en dualboot ( sur une installation en dur)

## Setup/Installation Requirements



     instalation  de oracle VM virtualbox et de machines virtuelles Linux : https://docs.oracle.com/cd/E26217_01/E35193/html/qs-preface.html
          Archlinux ( https://archlinux.org/)  et Ubuntu https://brb.nci.nih.gov/seqtools/installUbuntu.html
          Language de programmation supporté par les 2 distributions : Python 3.9 et SQL
                    Commande pour installer python  Archlinux : sudo pacman -S Python3-pip for Python in an Arch Linux terminal.
                    Commande pour installer python  Ubuntu  : sudo apt install -y python3-pip

                    Commande pour installer SQL Archlinux : 
                    Commande pour installer SQL Ubuntu : sudo apt-get update    
                                                         sudo apt-get upgrade   
                                                         sudo apt-get install -y mssql-server


                    
          installer la distribution de votre choix (aucun probleme de comptabilité de language avec python)
          le language du serveur SQL mariaDB est aussi supporté par les 2 distributions linux ( seule les commandes en terminal de commande et les commandes d'installations différent)

     # installation de vs code: https://code.visualstudio.com/download 
               tutuoriel from  freeCodeCamp.org :  Visual Studio Code Full Course - VS Code for Beginners https://www.youtube.com/watch?v=UTQp6mvhb0Y


     
     # clone du répertoire : https://github.com/Faralinn/projet_spotifree_group1/tree/sql
          -> de la branche  team_python : https://github.com/Faralinn/projet_spotifree_group1/tree/team_python
          -> de la branche  team_SQL :  https://github.com/Faralinn/projet_spotifree_group1/tree/sql 
          -> notre repository : https://github.com/Faralinn/projet_spotifree_group1
          -> how to clone a repository on github : https://www.atlassian.com/fr/git/tutorials/setting-up-a-repository/git-clone

## Technologies and modules  Used##
"""" 
     #_Python_(documentation https://docs.python.org/3/) :

     L'installation des modules dans python se fait a l'aide de pip. pip est l'outil d'installation de prédilection. À partir de Python 3.4, il est inclus par défaut avec l'installateur de Python.
                    -> documentation : https://docs.python.org/fr/3.10/installing/index.html
                    -> tutoriel: https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-comment-travailler-avec-le-package-pip-en-python
                    -> commande CLI : sudo apt update && sudo apt install python3-pip
     Quelques commandes utiles avec pip  sous python:
                                                       pip help install : montre l'aide complète sur la commande install.
                                                       pip search matplot : pour chercher tous les packages qui ont matplot dans le nom ou la description.
                                                       pip install matplotlib : pour installer le package matplotlib et ses dépendances (sous root).
                                                       pip install -U matplotlib : pour mettre à jour le package.
                                                       pip uninstall matplotlib : pour désinstaller le package (sous root).
                                                       pip list : pour lister les packages installés.
                                                       pip show matplotlib : donne les infos sur un package (description, version, dépendances).
                                                       pip show -f matplotlib : montre en plus les fichiers installés pour le package.
                                                       pip check : vérifie les requirements de tous les packages
                                                       pip list -o : liste les packages qui ne sont plus à jour.


## concept de base du python socket
 python socket : (documentation https://docs.python.org/3/library/socket.html)
-Le socket est  dans notre cas une association au niveau de l'OS entre un programme qui tourne en boucle et le port de la machine qui lui a été dédié. On dit d'ailleurs que le programme écoute le port qui lui a été réservé. Il écoute le port et répond aux demandes faites par ce port.
les commandes et le fichier client sont consignés dans le file client      
           un client : -> "import socket"      

          un serveur :-> "import socket from _thread import *"



## Modules Python ( for sockets)
L'installation des modules dans python se fait a l'aide de pip. pip est l'outil d'installation de prédilection. À partir de Python 3.4, il est inclus par défaut avec l'installateur de Python.
                    -> documentation : https://docs.python.org/fr/3.10/installing/index.html
                    -> tutoriel: 
                    -> commande CLI : sudo apt update && sudo apt install python3-pip

#Pandas : permet la création d'un dataframe et son importation en csv pour importation dans MariaDB
                    -> pandas 1.4.2 : https://pypi.org/project/pandas/
                    -> documentation : https://pandas.pydata.org/docs/
                    -> Tutoriel :    https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-comment-installer-et-utiliser-pandas
                    -> commande CLI : pip install pandas
                    

#Spotipy : est une bibliothèque Python  pour l' API Web Spotify; Elle permet d'effectuer des recherches dans l'API Spotify via pythonvous obtenez un accès complet à toutes les données musicales fournies par la plateforme Spotify.Ce module fonctionne avec les définition de variables d'environnement telque SPOTIPY_CLIENT_ID. 
                    -> spotipy 2.19.0 : https://pypi.org/project/spotipy/
                    ->Tutoriel : https://www.erwanlenagard.com/musique/creer-une-playlist-de-recommandations-spotify-1341
                    -> documentation: https://spotipy.readthedocs.io/en/2.19.0/
                    -> commande CLI : pip install spotipy


#Time : le module time permet de gérer des fonctions liées au temps définit par ce module. exemple  dans Python time.sleep().ici sleep()fonction suspend (retarde) l'exécution du thread en cours pendant le nombre de secondes donné.
                    -> tutoriel : https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-comment-dfinir-les-modules-temps-en-python
                    -> documentation :https://docs.python.org/3/library/time.html
                    ->  script python : import time 

#re : (Regular expression operations) : module Python standard re qui nous permet d'utiliser les expressions régulières
     -> tutoriel : https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-matriser-le-module-regex-en-python
     -> documentation :  https://docs.python.org/3/library/re.html
     -> Script python : import re 


## BASE DE DONNEES SQL / MARIADB

     #_SQL/MariaDB_ (documentation https://wiki.archlinux.org/title/MariaDB):
MariaDB est un système de gestion de base de données relationnelle (SGBDR) open source qui constitue une solution de remplacement compatible avec la technologie très répandue des bases de données MySQL. Ce système a été créé sous la forme d'un dérivé logiciel (fork) de MySQL.MariaDB repose sur SQL et prend en charge le traitement de données selon le modèle ACID, c'est-à-dire avec garantie d'atomicité, de cohérence, d'isolation et de durabilité des transactions. Entre autres fonctionnalités, la base de données prend en charge les API JSON, la réplication parallèle des données et de nombreux moteurs de stockage, dont InnoDB, MyRocks, Spider, Aria, TokuDB, Cassandra et MariaDB ColumnStore.

 L'installation se fait à partir d'un terminal de commande (CLI).
          Commande d'installation de Mariadb sur Ubuntu :
                                                       sudo apt update
                                                       sudo apt-get -y install mariadb-server
                                                       sudo mysql_secure_installation
                                                       sudo systemctl start mariadb
                                                       sudo systemctl enable mariadb
          Commande d'installation de Mariadb sur Archlinux :  
                                                       mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql  

## Getting started with MariaDB <a name="introduction"></a> [MariaDB](https://mariadb.com) 
 MariaDB est un serveur soutenu par une communauté de devellopeur , vous pouvez trouvez plus d'information sur son téléchargement installation et utilisation  [MariaDB Quickstart Guide](https://github.com/mariadb-developers/mariadb-getting-started).



## Modules Python pour SQL/MariaDB

#sqlalchemy:  SQLAlchemy donne à vos programmes une fonctionnalité de base de données, vous permettant de stocker des données dans un seul fichier sans avoir besoin d'un serveur de base de données. SQLAlchemy est un ORM (Object-Relational Mapping) permettant de synchroniser vos classes avec des tables en base de données relationnelle (basée sur SQL). L'étape la plus importante, quand on utilise un ORM, c'est de réaliser le « Mapping », c'est à dire l'association entre les éléments de vos classes et ceux de vos tables en base de données (https://www.fullstackpython.com/object-relational-mappers-orms.html)
                    -> tutoriels : https://docs.sqlalchemy.org/en/14/tutorial/index.html
                                   https://www.youtube.com/watch?v=6k6NxFyKKQo
                                                                 
                    -> documentation : https://docs.sqlalchemy.org/en/14/orm/mapping_columns.html
                                       https://riptutorial.com/Download/sqlalchemy-fr.pdf
                    -> Script python :  import sqlalchemy
                                        from sqlalchemy.ext.declarative import declarative_base
                                        from sqlalchemy import create_engine
#create_engine :
                    -> tutoriel : exemples de scripts (https://www.programcreek.com/python/?CodeExample=create+engine)
                    -> documentation : https://docs.sqlalchemy.org/en/14/core/engines.html
                    -> Script python :  from sqlalchemy import create_engine             
#mariadb :                                                

## Module CSV :
#os :
#eyes :
#glob : 

"""
# Docker Client : construction d un containeur

Le logiciel open source Docker s’est imposé comme la norme de la virtualisation des conteneurs d’applications. La virtualisation des conteneurs est le prolongement du développement des machines virtuelles, à une différence fondamentale près : au lieu de simuler un système d’exploitation complet, une seule application est virtualisée dans un seul conteneur.
Docker est piloté sur le système local via une interface en ligne de commande. 
Un conteneur est assez semblable à une VM. Alors que la VM est une machine entièrement nouvelle (d’un point de vue software) construite sur une machine physique, un conteneur n’a de son côté pas tous les composants habituels d’une machine a habituellement. Pour être plus précis, il n’a pas d’OS entier, mais seulement ce qui est nécessaire pour faire tourner ses applications. Il est construit à partir d’une image, qui correspond à sa configuration.les commandes Docker ne concernent qu’un seul conteneur (ou image) à la fois, alors que Docker-compose gère plusieurs conteneurs Docker. 

pour mieux connaitre cette technologie vous pouvez regarder le tutoriel suivant : 
                                                       Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers from freeCodeCamp.org :https://www.youtube.com/watch?v=fqMOX6JJhGo


               pour plus de documentation: 
[![codecov](https://codecov.io/github/spotify/docker-client/coverage.svg?branch=master)](https://codecov.io/github/spotify/docker-client?branch=master)
     L'installation se fait à partir d'un terminal de commande (CLI).
                                                                 Installation de Docker sur Ubuntu :
               ( tutoriel : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-fr):
               Les commandes   Docker sur Ubuntu : 
                                    d'installation :  apt install docker-compose
                                    Désinstaller les anciennes versions avec la commande sudo apt-get remove docker docker-engine docker.io containerd runc 
                                    configuration des dépots par la mise à jour de apt : sudo apt-get update
                                    Installer les paquets permettant à APT d'utiliser un serveur HTTPS de dépôt :  sudo apt-get install \
                                                                                                                   apt-transport-https \
                                                                                                                   ca-certificates \
                                                                                                                   curl \
                                                                                                                   software-properties-common  

                                    Puis ajouter la clé GPG du site de Docker :curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
                                    Pointer vers le dépôt de la version "stable" de docker CE : echo \
                                                                                               "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
                                                                                               $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 

                                                                           Installer Docker CE : sudo apt-get update
                                                                           Installer la dernière version de Docker Engine et containerd :sudo apt-get install docker-ce docker-ce-cli containerd.io


                                                                  Installation de Docker sur Archlinux : https://archlinux.org/packages/community/x86_64/docker-compose/
                                                                  Documentation Archlinux : https://docs.docker.com/desktop/linux/install/archlinux/
tutoriel : How to Install Docker on Linux 2021 | Installing Docker on Arch | Docker Installation on Linux from TechSolutionZ : https://www.youtube.com/watch?v=ynFlgkKzxOY
           How to Install Docker + Docker Desktop on Arch Linux/Arch based Distributions! | Easy Guide from Agam's Tech Tricks : https://www.youtube.com/watch?v=tOMt71hMnM0

                          Prérequis il faudra un environnement gnomes pour les environnement initialement no gnome avec la commande :sudo pacman -S gnome-terminal

Commandes de lancement de Docker :
                          Installer Docker Desktop :  sudo pacman -U ./docker-desktop-<version>-<arch>.pkg.tar.zst
                          Lancer Docker Desktop : systemctl --user start docker-desktop puis les prochaines connexions systemctl --user enable docker-desktop, pour l'arrêter systemctl --user stop docker-desktop
                          sinon mamuellement  dans le menu Docker, sélectionnez Paramètres > Général > Démarrer Docker Desktop lorsque vous vous connectez, pour l'arrêter cliquez sur l'icône de la barre de menu baleine pour ouvrir le menu Docker et sélectionnez Quitter Docker Desktop.
Commandes de monotoring  de Docker :
                              > docker ps (-a) : affiche toutes les instances de docker qui tournent actuellement sur votre environnement. 
                              > docker images (-a) : montre les images que vous avez construites, et le -a vous montre les images intermédiaires.
                              > docker network ls : liste les différents réseaux et docker-compose
                              > docker-compose ps : affiche tous les containers qui ont été lancés par docker-compose (qu’ils tournent actuellement ou non).

Commandes de run time :
                              > docker-compose up (-d) (--build) : va construire vos images si elles ne le sont pas déjà, et va démarrer vos dockers. Si vous voulez re-build vos images, utilisez l’option --build (vous pouvez aussi utiliser la commande docker-compose build pour uniquement construire des images). L’option -d, qui signifie "detach" fait tourner les conteneurs en tâche de fond.
                              > docker-compose stop : stop mais ne supprime pas les conteneurs
                              > docker build (-t NAME ) PATH /URL :  construire votre image, où vous pouvez spécifier le nom de votre image et vous devez spécifier le PATH ou URL selon votre contexte (cela peut être un repo git).
                              > docker run (-d) (-p hostPort :containerPort ) (--name NAME ) IMGNAME /IMGID :run crée le conteneur en utilisant l’image que vous indiquez. Vous pouvez spécifier de nombreux paramètres. Nous vous recommandons d’ajouter un nom à votre conteneur et vous pourriez avoir besoin de spécifier quelques ports à exposer. Comme pour docker-compose, le -d lance le conteneur en tâche de fond. 
                              > docker start ID /NAME : “start” uniquement des conteneurs qui sont déjà arrêtés, donc déjà build avec la commande run.
                              > docker stop ID /NAME : arrête  votre container
                              > docker exec -it NAME /ID “sh” /”/bin/bash” : Cette commande vous permet de lancer un shell sur votre container. 


## Docker nombre de connexions 



## Docker ftp 


Docker compose aide a l'orchestration de container, pour plus d 'information  [example of the docker compose](https://github.com/stilliard/docker-pure-ftpd/blob/master/docker-compose.yml). 
image du docker FTP https://hub.docker.com/r/delfer/alpine-ftp-server

`docker run -d -v /home/camille/Musique:/home/vsftpd -p 21:21 -e FTP_USER=vsftpd -e FTP_PASS=passwd --name server_ftp --restart=always fauria/vsftpd`
#pour se connecter à distance: ftp <ip_server>

## Docker mariadb

#Crétation d'un network appelé <some-network>
`docker network create some-network`
#Création du docker avec un user, mot de pass et un mot de pass pour root
`docker run --detach --network some-network --name spoti_mariadb --env MARIADB_USER=spoti --env MARIADB_PASSWORD=spotipass --env MARIADB_ROOT_PASSWORD=spotipass mariadb:latest`
#Lancement de mariadb via le docker
`docker run -it --network some-network --rm mariadb mysql -h spoti_mariadb -u root -p`
#Création de la base de donnée spotifree
`CREATE DATABASE spotifree;`
`exit`
#Import du script SQL pour création des tables
`docker exec -i spoti_mariadb mysql -u root -p spotipass spotifree < /home/camille/Documents/spotifree_user_bdd.sql`

#Ligne de commande pour entrer dans le docker mariadb:
#`docker run -it --network some-network --rm mariadb mysql -hspoti_mariadb -uroot -p`

## Docker jenkins










     
     
