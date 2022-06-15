import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas
import time 
import re 
#Import pour la partie sql
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import mariadb
#Import pour méthadonnée des fichiers mp3
import eyed3
import os, glob, eyed3
#spotipy : permet d'effectuer des recherches dans l'API Spotify via python
#pandas : permet la création d'un dataframe et son importation en csv pour importation dans MariaDB
#time permet d'importer la fonction sleep. re permet d'utiliser des expression régulières


#bloc authentification à l'API spotify
client_id='c26e4786d0d448f88c5acdbbf521ad83'
client_secret ='49e36cac584b4271a98873099ca92b7b'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#fonction permettant d'extraire l'id d'un artiste depuis son nom
#Si plusieurs résultats à cause d'homonymes ou d'une recherche trop peu précise, l'artiste le plus populaire est choisi
#Amélioration possible : trouver les n premiers artistes et donner le choix à l'utilisateur en modifiant le paramètre "limit" dans sp.search
def getArtist(searchOnSpotify):
    artist_data = sp.search(q='artist:' + searchOnSpotify,limit=1, type='artist')
    id=artist_data['artists']['items'][0]['id']
    name=artist_data['artists']['items'][0]['name']
    popularity=artist_data['artists']['items'][0]['popularity']
    #print(artist_data['artists']['items'][0]['external_urls']['spotify'])


    print('--------------------------------------------------------------')
    print('------------------------Infos Artiste-------------------------')
    print('--------------------------------------------------------------')
    print("Name : ",name," - Popularity : ",popularity,"/ 100")

    return id #on retourne l'id de l'artiste


#fonction prenant en paramètre l'id d'un artiste et retournant la liste des id de ses albums
def getArtistAlbums(artist_id):

    albums_data = sp.artist_albums(artist_id)
    albums=[]
    albums_id=[]
    names=[]                                                #on stocke les noms des albums pour supprimer les doublons

    for album in albums_data['items'] :
        id=album['id']
        raw_name=album['name']
        name = re.sub("\s*\(Deluxe\)\s*", "", raw_name)     #suppression des "Deluxe" dans les albums à cause de trop nombreux doublons
        
        data_album=[id,name]
        if name not in names :                              #si on a pas encore stocké le nom de l'album, on le rajoute à la liste
            names.append(name)
            albums.append(data_album)
            albums_id.append(id)

    print('--------------------------------------------------------------')
    print('-------------------------Infos Albums-------------------------')
    print('--------------------------------------------------------------')
    for album in albums :
        print("Album name : ",album[1])
    
    return albums_id #on retourne la liste des ids des albums de l'artiste


#fonction prenant en paramètre l'id d'un album et retournant la liste de ses musiques
def getAlbumTracks(album_id):

    tracks_data = sp.album_tracks(album_id)
    tracks=[]
    tracks_id=[]

    for track in tracks_data['items'] :
        id=track['id']
        name=track['name']
        data_track=[id,name]
        tracks.append(data_track)
        tracks_id.append(id)

    # print('--------------------------------------------------------------')
    # print('------------------------Infos Musiques------------------------')
    # print('--------------------------------------------------------------')
    # for track in tracks:
    #     print("Track name : ",track[1])

    return tracks_id #on retourne la liste des ids des musiques de l'album


#fonction prenant en paramètre l'id d'une musique et retournant une liste de ses caractéristiques
#"meta" contient les caractériqtiques principales, "features" contient des caractéristiques optionnelles 
# pouvant être utilisées pour implémenter des fonctionnalités supplémentaires ultérieurement
def getTrackData(id_track):
    meta = sp.track(id_track)
    #features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # # features
    # acousticness = features[0]['acousticness']
    # danceability = features[0]['danceability']
    # energy = features[0]['energy']
    # instrumentalness = features[0]['instrumentalness']
    # liveness = features[0]['liveness']
    # loudness = features[0]['loudness']
    # speechiness = features[0]['speechiness']
    # tempo = features[0]['tempo']
    # time_signature = features[0]['time_signature']

    track = [id_track, name, album, artist, release_date, length, popularity] #, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track





#Fonction prenant en paramètre le nom d'un artiste et générant un .csv contenant l'ensemble des titres et caractéristiques associées de l'artiste
def getDiscography(artist_name):
    discography=[]
    track_names=[]
    artist=getArtist(artist_name)
    albums=getArtistAlbums(artist)
    
    os.chdir("/home/arthur/Musique/") #Chemin où se trouve la musique
    online="" 
    for album in albums:
        tracks=getAlbumTracks(album)
        for id_track in tracks:
            track_data=getTrackData(id_track) 
            
            for file in glob.glob("*.mp3"): #Boucle pour vérifier la disponibilité de la musique dans le dossier
                eyed3.log.setLevel("ERROR")
                audiofile = eyed3.load(file)          
                if audiofile.tag.artist.casefold() == track_data[3].casefold() and audiofile.tag.title.casefold() == track_data[1].casefold():
                    online = "Dispo"
                else:
                    online = "non-dispo"
            track_data.append(online)            

            if track_data[1] not in track_names:
                track_names.append(track_data[1])
                discography.append(track_data)
    print ("#####################",track_data)

    df = pandas.DataFrame(discography, columns = ['id','title', 'album', 'artist', 'release_date', 'length', 'popularity', 'dispo']) 
    #, 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
    engine = create_engine("mariadb+mariadbconnector://thurux:thurux@localhost:3306/spotifree")
    df.to_sql('listing', engine, if_exists='append', index = False)
    


# query=input("Quel Artiste : ")
# getDiscography(query)