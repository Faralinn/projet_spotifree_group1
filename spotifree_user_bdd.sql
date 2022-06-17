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
CREATE TABLE playlists (
    titre_playlist VARCHAR(30) PRIMARY KEY,
    utilisateurs TEXT,
    droits TEXT
);

/* création d'une table pour chaque playlist, ici playlist test */
CREATE TABLE playlist_test (
    titre_playlist VARCHAR(30) PRIMARY KEY,
    artist TEXT,
    musique TEXT,
    FOREIGN KEY (titre_playlist) REFERENCES playlists (titre_playlist)
) ENGINE = InnoDB;

/* création table liste amis */

CREATE TABLE spotifriends (
    pseudo VARCHAR(30) PRIMARY KEY,
    amis TEXT,
);

INSERT INTO playlists VALUES (
    "playlist_test",
    "arthur",
    "privée"
);

INSERT INTO playlist_test VALUES (
    "playlist_test",
    "jack white",
    "entitlement"
);

INSERT INTO identifiants VALUES (
    "cannelle",
    "secret"
);

INSERT INTO identifiants VALUES (
    "arthur",
    "arthurus"
);

INSERT INTO identifiants VALUES (
    "soufian",
    "socket"
);

INSERT INTO identifiants VALUES (
    "AyetImen",
    "1213"
);

INSERT INTO identifiants VALUES (
    "albert",
    "password"
);

INSERT INTO identifiants VALUES (
    "gertrude",
    "password"
);


CREATE TABLE listing (
    id TEXT,
    title TEXT,
    album TEXT,
    artist TEXT,
    release_date TEXT,
    length TEXT,
    popularity TEXT,
    dispo TEXT
);
