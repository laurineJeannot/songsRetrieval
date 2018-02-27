import os
"""
    This module will allow to prepare the data for using it in the search engine

    You will find the functions :
    - stopwordsDelete: for a giving song, delete all the stopwords
    -
"""

def stopwordsDelete(filename):
    '''
    1st: open the files used to compare the words
    2nd: for each song, delete the stopwords in the list of tokens
    :param filename: file to apply the function
    :return: modified file (without stopwords in the songs)
    '''
    stopwords = open("stopwords.txt").readline().split(",")
    wordsId = open("wordId.txt").readline().split(",")
    songs = open(filename).readlines()
    stopwordsDeleted = open("resultScript.txt",'a')
    for song in songs:
        song = song.split(",")
        for word in song[2:]:
            idSong = int(word.split(":")[0])
            if wordsId[idSong] in stopwords:
                song.remove(word)
        song = str(song)
        stopwordsDeleted.write(song+"\n")
    stopwordsDeleted.close()

os.chdir("C:/Users/Laurine/Desktop/coursSciencesCo/S8/Information Retrieval/songsRetrieval")
stopwordsDelete("scriptTest.txt")
