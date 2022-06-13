/* date: 13/06/2022*/
/*Script sql pour la création de la database "spotifree" avec différentes tables*/


/* création database + positionnement pour ajout des tables*/

DROP DATABASE spotifree;
CREATE DATABASE spotifree;
USE spotifree;


/* création table user + password*/

CREATE TABLE identifiants (
    pseudo VARCHAR(30) PRIMARY KEY,
    mot_de_pass TEXT
);


/* création table playlist */

CREATE TABLE playlist (
    pseudo VARCHAR(30) PRIMARY KEY,
    titre_playlist TEXT,
    musique TEXT
);


/* création table liste amis */

CREATE TABLE spotifriends (
    pseudo VARCHAR(30) PRIMARY KEY,
    amis TEXT
);




