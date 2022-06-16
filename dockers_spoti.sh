#!/bin/bash

###Script pour création des dockers


## Docker ftp 

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

