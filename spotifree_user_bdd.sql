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
    pseudo VARCHAR(30),
    titre_playlist TEXT,
    artist TEXT,
    musique TEXT,
    FOREIGN KEY (pseudo) REFERENCES identifiants (pseudo)
) ENGINE = InnoDB;


/* création table liste amis */

CREATE TABLE spotifriends (
    pseudo VARCHAR(30) PRIMARY KEY,
    amis TEXT,
    FOREIGN KEY (pseudo) REFERENCES identifiants (pseudo)
) ENGINE = InnoDB;





INSERT INTO identifiants VALUES (
    "cannelle",
    "root"
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
    name TEXT,
    album TEXT,
    artist TEXT,
    release_date TEXT,
    length TEXT,
    popularity TEXT
);


