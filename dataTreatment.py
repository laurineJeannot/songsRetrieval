import os
import re
from song import Song
from nltk.corpus import wordnet as wn

"""
    This module will allow to prepare the data for using it in the search engine

    You will find the functions :
    - stopwordsDelete: for a giving song, delete all the stopwords
    - getWordsId: gets the word list


    - firstsTreatmentsOnFiles: final method writing the treated data
"""

def stopwordsDelete(filename):
    '''
    1st: open the files used to compare the words
    2nd: for each song, delete the stopwords in the list of tokens
    :param filename: file to apply the function
    :return: modified file (without stopwords in the songs)
    '''
    print(filename)
    stopwords = open("stopwords.txt").readline().split(",")
    wordsId = getWordsId()
    songs = open(filename).readlines()
    stopwordsDeleted = open(filename[:-4]+"Result.txt",'a')
    for song in songs:
        song = song.split(",")
        for word in song[2:]:
            idSong = int(word.split(":")[0])
            if wordsId[idSong] in stopwords:
                song.remove(word)
        song = str(song)
        stopwordsDeleted.write(song+"\n")
    stopwordsDeleted.close()

def getWordsId():
    """
    returns a the list of words and their place in the list is their id
    """
    return open("wordId.txt").readline().split(",")

def getListOfSongsAndWords(filename):
    """
    return a list of the form
    [
    ['TRAAPKW128F428BC93', '5427582', '1:10', '2:7', '3:2', ...]
    ['TRAAPKS128F92F9047', '1894097', '2:16', '3:5', '5:6', ...]
    ...
    ]
    """
    songs = open(filename).readlines()[18:]
    # f[17] is the list of words
    # f[18] is the first song
    for i, s in enumerate(songs) :
        if "\n" in s : s = s[:-1]
        songs[i] = s.split(",")
    return(songs)

def getListOfGlobalSongData():
    """
    return a list of the form 
    [
    [tid,artist name,title,mxm tid,artist_name,title],
    ... 
    ]
    """
    # f[17] is the last commentary
    # f[18] is the first song
    songs = open("corpus//mxm_779k_matches.txt",encoding="utf-8").readlines()[18:]
    for i, s in enumerate(songs) :
        if "\n" in s : s = s[:-1]
        songs[i] = s.split("<SEP>")
    return(songs)

def getMostUsedWords(song,n):
    #TODO list the most used words in the song
    song = song.split(",")[2:]
    listeTriee = []
    for word in song:
        regex = re.compile(r'(\d*):(\d*)')
        listeTriee.append(regex.search(word).groups())
    listeTriee = sorted(listeTriee, key=lambda x: x[1],reverse=True)
    return(listeTriee[0:n])

def generateLexicalFields(word,n):
    #TODO take a word and generates n hypernyms with wordnet
    hypernymList = []
    hyponymList = []
    for word in words:
        wordSyn = wn.synsets(word)
    #on cherche les hyponymes
    if wordSyn!=[]:
        for synset in wordSyn[0:n]:
            hypernymList.append(synset.hypernyms())
            for elt in hypernymList:
                hyponymList = elt.hyponyms()
    #on formate les lexemes
    for word in hyponymList:
        word = word.replace("Synset('","")
        word = word.replace(word[-7:],"")
    return hyponymList

def writeResults(trackIds,words):
    #TODO write all the results in a single txt file
    '''
    Structure d'une ligne : trackId1;trackId2;mostUsedWords;lexicalFields
    '''
    file = open("finalData.txt","w")
    resu = str(trackIds[0]+";"+trackIds[1]+";")
    for word in words:
        resu = resu + word +"("
        lexField = generateLexicalFields(word,5)
        for elt in lexField:
            resu = resu + elt +";"
        resu = resu + ")"
    file.write(resu)
    file.close()

def firstsTreatmentsOnFiles():
    """
    open our 3 corpus files
    delete stop words
    get the most used words
    generate lexical fields and score
    write song info, lexical fields, most used words into result file
    """
    directory="corpus\\"
    corpus_filenames = ["mxm_dataset_test-test.txt","mxm_dataset_train-test.txt"]
    songData_filename = "mxm_779k_matches.txt"

    """
    ============================================================
    Use stopwordsDelete function on every file, update the names
    ============================================================
    """
    # for i, filename in enumerate(corpus_filenames):
    #     stopwordsDelete(directory+filename)
    #     corpus_filenames[i] = filename+"Result.txt"

    """
    ============================================================
    Generate Lexical fields
    ============================================================
    """
    wordsId = getWordsId() 
    #data with artist and song name
    songGlobalData = getListOfGlobalSongData()
    for filename in corpus_filenames:
        songListWithWords = getListOfSongsAndWords(directory+filename)
        n = 5
        for s in songListWithWords :
            song = Song(s[0],s[1])
            words = getMostUsedWords(s,n)
            print(words)
            #j'ai enlevé la fonction generateLexicalFields ici car je les génère dans l'écriture des résultats
            trackIds = song.split(",")[0:2]
            writeResults(trackIds,words)

    """
    ============================================================
    Get artist and Title
    ============================================================
    """
            for w in words :
               generateLexicalFields(w,n)
            #Get artist and Title
            #cette partie est déjà très longue en soit attention
            for sd in songGlobalData :
                if song.tid == sd[0] :
                    song.artist = sd[1]
                    song.title = sd[2]
                    print(song)

    """
    ============================================================
    Write the results
    ============================================================
    """
    #déplacé dans "Generate Lexical Fields" pour enregistrer la ligne au fur et à mesure

firstsTreatmentsOnFiles()
