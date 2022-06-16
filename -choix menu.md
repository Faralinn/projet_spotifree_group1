-choix menu
    -wide_recherche:
    => par artiste => getDiscography => recherche sql table = artiste condition = input => si dans ftp => DL
            if by_artist:
                table=artiste
                condition=input("Entrez le nom de l'artiste : ")
                getDiscography(input)
                reply=str(search(condition,table) = requête SQL) => send with socket
                if colonne_download non null
                    fonction_download(reply) => choix download 
                        if choix_download:
                            requête server ftp
    => par album => getDiscography => recherche sql table = album condition = input => si dans ftp => DL
            if by_album:
                table=album
                condition=input("Entrez le nom de l'album : ")
                getDiscography(input)
                reply=str(search(condition,table) = requête SQL) => send with socket
                if colonne_download non null
                    fonction_download(reply) => choix download 
                        (test_down => requete sql => test si colonne null ou non)_if choix_download:
                            requête server ftp
    => par musique => getDiscography => recherche sql table = musique condition = input => si dans ftp => DL
            if by_musique:
                table=musique
                condition=input("Entrez le nom de la musique : ")
                getDiscography(input)
                reply=str(search(condition,table) = requête SQL) => send with socket
                if colonne_download non null
                    fonction_download(reply) => choix download 
                        if choix_download:
                            requête server ftp


#################
-gestion_playlist
-Playlists
        lister Playlist -> "que voulez-vous faire ?"
            -selectionner playlist
                -modifier
                #-écouter
                -partager
                -supprimer
            -créer
            -retour menu
    
    -spotifriends
        lister amis -> "que voulez-vous faire ?"
            -selectionner ami
                -supprimer ami
                -envoyer message amis
            -ajouter ami
            -retour menu

