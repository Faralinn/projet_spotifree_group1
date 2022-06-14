import eyed3
import os


path="/home/camille/Musique/"
files = os.listdir("/home/camille/Musique")

for f in files:
    mpfile=path+f
    audiofile = eyed3.load(mpfile)

    #print(audiofile)
    print(audiofile.tag.artist)  #Récupération du nom de l'artist
    print(audiofile.tag.title)  #Récupération du titre de la chanson



