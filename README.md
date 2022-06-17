
  _________              __  .__  _____                       
 /   _____/_____   _____/  |_|__|/ ____\______   ____   ____  
 \_____  \\____ \ /  _ \   __\  \   __\\_  __ \_/ __ \_/ __ \ 
 /        \  |_> >  <_> )  | |  ||  |   |  | \/\  ___/\  ___/ 
/_______  /   __/ \____/|__| |__||__|   |__|    \___  >\___  >                                                                                      
              



###### creation d 'une application spotifree#####

#### auteurs  By _**Arthur GARRIGUE**_**_Cannelle DUGUET_**_**Soufian SAHLI**_**_Ayet Imen BERRADJ**_**Camille BARILLET **_
""" creation de deux teams :
- team Python : Arthur GARRIGUE, Soufian SAHLI, Cannelle DUGUET
- team SQL SQL Lite/SQL : Ayet Imen BERRADJ, Camille BARILLET

## Requirements :
"""" 
- serveur client
- sockets 
- gestions de base de données
- read me : nous avons essayer de partir du code python pour faire une intégration général de connaissance et aussi du déployement de l'application, ce read me est une explication de notre application et une mine de référence pour tous les débutants dans l'univers de la programmation et du devops . Bonne lecture!

## Fonctionnement de l'application    
Il nous a été donné comme projet de fin d'étude de coder une application similaire a spotify se nommant spotifree. Ce projet nous permet de revoir des notions de différentes technologies. l'application baptisé Spotifree  offre à l'utilisateur trois services essentiels (chercher de la musique, faire une playlist, et communiquer avec des amis).


**spotifree** est une application qui introduit la performance et la simplicité de l'utilisation de concepts informatiques comme les sockets en python, les bases des requetes SQL et du serveur MariaDB avec une 
            intégration continue sous la forme de docker
            
     #spotipy : permet d'effectuer des recherches dans l'API Spotify via python ; cette application pour son fonctionnement et en fonction du besoin neccessite l'installation  de plusieurs modules python ( pandas,....) . Au début du script python on fera appelle à ces modules par la fonction import +nom du module (ex import spotipy pour spotipy).

Notre application repose sur un script python qui interroge une base de données en SQL/MariaDB. Le script python fait appelle au socket python qui permet la communication entre un serveur et un client au travers de sockets. le script client est en interface de commande et communique à travers de son socket avec le socket du script serveur . Ce dernier le script serveur est lui aussi coder en python et a pour fonction essentielle de vérifier les requêtes client afin d'autoriser ou non la connexion à la base de données par le serveur en fonction de la demande du client.

La base de données ou BDD est stocké sur un serveur SQL; SQL est un ensemble de tables dans notre cas ( user, musique,spotifriend..) qui se lance en meme temps que le dockerfile pour une intégration continue sous forme de dockers . les dockers sont au nombre de 4 et posséde chacun leur spécificité :
                                                                                          1/ docker FTP
                                                                                          2/docker mariadb/SQL
                                                                                          3/docker python socket
pour assurer une connexion sécurisée à la base données des clefs SSH on été généré et l'intégration continue est assurée par un docker Jenkins ( avec un agent SSH).

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
 MariaDB est un serveur soutenu par une communauté de devellopeurs , 
 vous pouvez trouvez plus d'information sur son téléchargement installation et utilisation  [MariaDB Quickstart Guide](https://github.com/mariadb-developers/mariadb-getting-started).
 Voici une introduction aux bases de données : Database Systems - Cornell University Course (SQL, NoSQL, Large-Scale Data Analysis) https://www.youtube.com/watch?v=4cWkVbC2bNE&t=44s
                                           -> tutorial :MariaDB Tutorial For Beginners in One Hour by develop with Ahmad Mohey https://www.youtube.com/watch?v=_AMj02sANpI
                                           -> installation MariaDB (Beginner DevOps - How to Install MariaDB on Ubuntu by Alessandro Castellani https://www.youtube.com/watch?v=7H0manxJzFw&t=256s) 
                                           -> Create MariaDB Database and User by theurbanpenguin  (https://www.youtube.com/watch?v=SEgRK89UFFE) 
                                           ->  SQL Server Backup and Restore Tutorial (Part 1)  (https://www.youtube.com/watch?v=JpH77H20jg8)
                                           -> SQL Server Performance Essentials – Full Course by freeCodeCamp.org  https://www.youtube.com/watch?v=HvxmF0FUwrM&t=10s

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

#mariadb : utiliser le module mysql.connector pour nous connecter au serveur MariaDB ou MySQL et créer notre base de données permettant de stocker un catalogue de produits.
                    -> tutoriel : Connect Python to MariaDB/MySQL Database [Nearly everything you need to know in 9 minutes! by Discover Python   https://www.youtube.com/watch?v=oDR7k66x-AU                                           
                    -> documentation : https://mariadb.com/kb/en/about-mariadb-connector-j/
                    -> Script python : import mariadb

## Module CSV :  

Le module csv en Python permet d'analyser les fichiers CSV (Comma Separated Values). Un fichiers CSV contient des valeurs séparées par des virgules, que l'on utilise pour stocker des données tabulaires. En utilisant ce module, qui vient avec Python, nous pouvons facilement lire et écrire dans des fichiers CSV.
                    -> tutoriel : Fichiers CSV en Python || Tutoriel Python || Apprenez la programmation Python by Socratica(https://www.youtube.com/watch?v=Xi52tx6phRU)
                                  Python for Beginners: CSV Parsing (Part 1) - Parsing a Simple CSV File (https://www.youtube.com/watch?v=_r0jzrlcDPM)
                    -> Documentation : https://docs.python.org/fr/3/library/csv.html
## os : 

Le module os est un module  fournit par Python dont le but d'interagir avec le système d'exploitation, il permet ainsi de gérer l’arborescence des fichiers, de fournir des informations sur le système d'exploitation processus, variables systèmes, ainsi que de nombreuses fonctionnalités du systèmes. Le module os peut être chargé simplement avec la commande : import os.
                    -> tutoriel : Leçon 3 [Python : les modules] : le modules os par franck ebel (https://www.youtube.com/watch?v=KTh7AvnGkFU)
                    -> documentation : https://python101.pythonlibrary.org/chapter16_os.html
                    -> script python :    import os 
                    -> commandes (CLI) :  user = os.getlogin() 
                                          print(user) # imprime le nom d'utilisateur
                                          os.mkdir("c:/myFolder") # crée un dossier nommé myFolder sur le disque C:\
                                          os.getcwd() : renvoie le répertoire actuel sous forme de chaîne de caractères.
                                   
Afin de pouvoir utiliser la méthode os.path, il faut préalablement importer le module pathlib. Le module pathlib est un module doté d'une interface orientée objet inclus dans python depuis la version 3.4. La méthode os.path.exist() permet de tester si un répertoire existe ou non

## Module eyes :

la fonction numpy.eye() en Python est utilisée pour renvoyer un tableau à deux dimensions avec des uns (1) sur la diagonale et des zéros (0) ailleurs.
                              -> tutoriel : 
                              -> documentation:
                              ->commandes et syntaxe :
                              numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
La fonction numpy.eye() prend les valeurs de paramètres suivantes :

                              N: Cela représente le nombre de lignes que nous voulons dans le tableau de sortie.
                              M: Cela représente le nombre de colonnes que nous voulons dans le tableau de sortie. Ceci est facultatif.
                              k: Ceci représente l'indice de la diagonale. 0est la valeur par défaut et la diagonale principale. Ceci est facultatif.
                              dtype: Cela représente le type de données du tableau à retourner. Ceci est facultatif.
                              order: Cela représente si la sortie doit être stockée Cou Fordonnée en mémoire. Ceci est facultatif.
                              like: Il s'agit du prototype ou de l' array_likeobjet du tableau.
                                   

## Module glob : 
Le module glob recherche tous les chemins correspondant à un motif particulier selon les règles utilisées par le shell Unix, les résultats sont renvoyés dans un ordre arbitraire. Aucun remplacement du tilde n'est réalisé, mais les caractères *, ?, et les caractères [] exprimant un intervalle sont correctement renvoyés. Cette opération est réalisée en utilisant les fonctions os.scandir() et fnmatch.fnmatch() de concert, et sans invoquer une sous-commande. Notons qu'à la différence de fnmatch.fnmatch(), glob traite les noms de fichiers commençant par un point (.) comme des cas spéciaux. En Python, le module glob est utilisé pour récupérer les fichiers / chemins correspondant à un modèle spécifié. Les règles de modèle de glob suivent les règles standard d’expansion de chemin Unix. Il est également prédit que selon les benchmarks, il est plus rapide que les autres méthodes de faire correspondre les noms de chemins dans les répertoires. Avec glob, nous pouvons également utiliser des caractères génériques en ("*, ?, [ranges])
                    -> exemple de commande en script python 
                                                  import glob 
                                                  print('Named explicitly:') 
                                                  for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'): 
                                                        print(name) 

                    -> documentation : https://docs.python.org/fr/3.11/library/glob.html
                    -> tutoriel : glob in Python (Complete Explanation with Examples) by Indian Pythonista https://www.youtube.com/watch?v=Vc5kGYty18k
                               python glob module|glob.glob pattern in python|| Python Tutorial #10|| Python Tutorial for Beginners by Code4You https://www.youtube.com/watch?v=qnWqJqV6mtY
                    



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


## Docker ftp 

Docker compose aide a l'orchestration de container, pour plus d 'information  [example of the docker compose](https://github.com/stilliard/docker-pure-ftpd/blob/master/docker-compose.yml). 
image du docker FTP https://hub.docker.com/r/delfer/alpine-ftp-server. 
                                                           -> image docker https://hub.docker.com/r/docker/compose
                                                           -> commande : docker pull docker/compose

Nous avons utilisé FORIA FTPD + JENKINS
                          -> commande :docker pull fauria/vsftpd
                         -> image docker fauria/vsftpd : https://hub.docker.com/r/fauria/vsftpd/
                         -> tutoriel Utilisation de docker pour installer nginx et vsftpd pour créer un serveur de fichiers: https://developpaper.com/using-docker-to-install-nginx-and-vsftpd-to-build-file-server/

`docker run -d -v /home/camille/Musique:/home/vsftpd -p 21:21 -e FTP_USER=vsftpd -e FTP_PASS=passwd --name server_ftp --restart=always fauria/vsftpd`
#pour se connecter à distance: ftp <ip_server>

## Docker mariadb

                                                            -> image docker mariadb : https://hub.docker.com/_/mariadb
                                                            -> commande: docker pull mariadb             


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

Jenkins est un outil open source de serveur d'automatisation. Il aide à automatiser les parties du développement logiciel liées au build, aux tests et au déploiement, et facilite l'intégration continue et la livraison continue. Écrit en Java, Jenkins fonctionne dans un conteneur de servlets tel qu’Apache Tomcat, ou en mode autonome avec son propre serveur Web embarqué. Lorsque vous installez Jenkins, son rôle dans le processus DevOps démarre une étape avant l'infrastructure, avec du code. Une équipe DevOps peut se reposer sur Puppet ou un outil DevOps similaire au bout du pipeline Jenkins et le faire fonctionner à partir de la plateforme.Jenkins est très proche de Java, bien qu'il puisse être utilisé avec Python et NodeJS par exemple. Le concept d’un build diffère en fonction du langage. On peut dire que Python, par exemple, n'a pas besoin de cette étape de build, mais nécessite tout de même celle du package.Jenkins peut également prendre en compte des scripts et des programmes de gestion de configuration (écrits en Salt) comme Ansible, Puppet, Chef, pour, par exemple, provisioner un cluster de VM ou des conteneurs Docker pour le test de charge. Il peut également les fermer, placer des réseaux virtuels ou configurer les ressources de stockage.

L'approche automatisée de bout en bout de Jenkins est idéale pour les projets de CI/CD.


L'outil open source d'intégration continue Jenkins est disponible sous la forme d'une image Docker proposée gratuitement sur le Docker Hub. Pour utiliser la dernière version stable de Jenkins (ou LTS) dans ce format, il suffit de lancer la commande suivante : docker pull jenkins/jenkins:lts
Pour recourir à la dernière version hebdomadaire de Jenkins au format Docker, voici la commande à utiliser : docker pull jenkins/jenkins
                                                       -> documentations : https://www.jenkins.io/doc/
                                                       -> tutoriels : gestion de la sécurité https://www.jenkins.io/doc/book/security/managing-security/
                                                                      gestion des plugins https://www.jenkins.io/doc/book/managing/plugins/
                                                                      utiliser les pipelines de jenkins https://www.jenkins.io/doc/tutorials/#pipeline
                                                                      mettre en oeuvre des builds dans jenkins https://www.jenkins.io/doc/tutorials/#tools


                                                         -> image docker jenkins : https://hub.docker.com/_/jenkins 
                                                         -> commande docker pull jenkins             

                                                       ->installation de jenkins
On lance une image jenkins : docker run --name jenkins-master -d -p 8080:8080 -p 50000:50000 -v /var/jenkins_home jenkins/jenkins:lts
Explication de la commande :
                              docker run : on lance une image
                              --name jenkins-master : on lui donne un nom
                              -d : en arrière plan
                              -p x:y : le port y de la machine virtuelle est mappée sur le port x de l'hote
                              -v chemin : on crée un volume pour garder les données de jenkins
                              jenkins/jenkins:lts : nom de l'image à utiliser (prise depuis hub.docker.com)
Une fois la machine lancée, on peut lancer un navigateur web et se connecter sur 127.0.0.1:8080.Après quelque temps, jenkins est prêt à être configuré. La première chose qu'il demande, est le mot de passe initial, pour cela, on demande à docker de nous récupérer un fichier dans la machine jenkins : docker cp jenkins-master:/var/jenkins_home/secrets/initialAdminPassword .
Il faut alors copier le contenu du fichier initialAdminPassword dans la page web qui la demandait.Il est alors demandé de sélectionner les plugins à installer, on peut garder les réglages par défaut.
On entre les informations de l'administrateur, et surtout, on clique sur "save & continue".On définit enfin à quelle adresse sera accessible le serveur.Jenkins est prêt à être utilisé.
Création d'un agent SSH
Maintenant, on va créer une seconde machine docker qui sera en charge de compiler notre projet.




                                                                                     
              _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
           _mN#F  aM"    #p"    !q@    9NL "9#Qu_
          g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
        _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
       j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
      ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
      F N"    #p"      Ng@       `#g"      "w@    "# t
     j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L
     0J  k _@   9g_ j#"   "b_  j#"   "b_ _d"   q_ g  ##
     #F  `NF     "#g"       "Md"       5N#      9W"  j#
     #k  jFb_    g@"q_     _*"9m_     _*"R_    _#Np  J#
     tApjF  9g  J"   9M_ _m"    9%_ _*"   "#  gF  9_jNF
      k`N    "q#       9g@        #gF       ##"    #"j
      `_0q_   #"q_    _&"9p_    _g"`L_    _*"#   jAF,'
       9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
        "b_ "#_    "NL      _B#      _I@     j#" _#"
          NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
           "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
              9##g_0@q__ #"4_  j*"k __*NF_g#@P"
                "9NN#gIPNL_ "b@" _2M"Lg#N@F"
                    ""P@*NN#gEZgNN@#@P""



     
     
