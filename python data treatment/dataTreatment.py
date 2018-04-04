import os
import re
from song import Song
from nltk.corpus import wordnet as wn
from langdetect import detect
import time

"""
    This module will allow to prepare the data for using it in the search engine

    You will find the functions :
    - getWordsId: gets the word list


    - firstsTreatmentsOnFiles: final method writing the treated data
"""

def getWordsId():
    """
    returns a the list of words and their place in the list is their id
    """
    with open("wordId.txt") as file : 
        return file.readline().split(",")

def getListOfSongsAndWords(filename):
    """
    return a list of the form
    [
    ['TRAAPKW128F428BC93', '5427582', '1:10', '2:7', '3:2', ...]
    ['TRAAPKS128F92F9047', '1894097', '2:16', '3:5', '5:6', ...]
    ...
    ]
    """
    with open(filename) as file :
        songs = file.readlines()[18:]
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
    songDict = {}
    with open("corpus//mxm_779k_matches.txt",encoding="utf-8") as file :
        songs = file.readlines()[18:]
    for i, s in enumerate(songs) :
        if "\n" in s : s = s[:-1]
        list = s.split("<SEP>")
        songDict[list[0]]=list[1:3]
    return(songDict)

def getMostUsedWords(song,n):
    """
    returns list of most used words in a song
    """
    song = song[2:]
    listeTriee = []
    for word in song:
        regex = re.compile(r'(\d*):(\d*)')
        listeTriee.append(regex.search(word).groups())
    listeTriee = sorted(listeTriee, key=lambda x: x[1],reverse=True)
    w = getWordsId()
    wordList = []
    with open("stopwords.txt") as file :
        stopwords = file.readline().split(",")
    for groups in listeTriee:
        i,j = groups
        word = w[int(i)]
        if word not in stopwords :
            wordList.append(w[int(i)])
        if len(wordList) == n : 
            break
    return(wordList)

def generateLexicalFields(words,n):
    """
    generates lf for each words of a song
    """
    hypernymList = []
    for word in words:
        wordSyn = wn.synsets(word)
        #on cherche les hyponymes
        if wordSyn!=[]:
            synset = wordSyn[0]
            if synset.hypernyms() != [] :
                hypernymList.append(synset.hypernyms()[0])
    for i,word in enumerate(hypernymList):
        hypernymList[i] = word.lemma_names()[0]
    return hypernymList

def writeResults(song):
    '''
    write all the results in a single txt file
    Structure of a line : tid,mxm_tid,title,artist,w:w1,w2,w3,w4,w5,lf:lf1,lf2...
    '''
    output = "collection/"+song.tid+".txt"
    with open(output,"w") as file :
        line = song.__str__()
        file.write(line+"\n")

def firstsTreatmentsOnFiles():
    """
    open our 3 corpus files
    delete stop words
    get the most used words
    generate lexical fields and score
    write song info, lexical fields, most used words into result file
    """
    directory="corpus\\"
    corpus_filenames = ["mxm_dataset_test.txt","mxm_dataset_train.txt"]
    songData_filename = "mxm_779k_matches.txt"


    """
    ============================================================
    Get song data and generate Words and Lexical fields
    ============================================================
    """
    wordsId = getWordsId() 
    #data with artist and song name
    songGlobalData = getListOfGlobalSongData()
    i = 0    
    for filename in corpus_filenames:
        songListWithWords = getListOfSongsAndWords(directory+filename)
        n = 5
        for s in songListWithWords :
            song = Song(s[0],s[1])
            #Get artist and Title
            song.artist = songGlobalData[song.tid][0]
            song.title = songGlobalData[song.tid][1]
            try :
                if (detect(song.title) == 'en'):
                    song.words = getMostUsedWords(s,n)
                    song.lexicalFields = generateLexicalFields(song.words,3)
                    writeResults(song)
            except :
                print("langage error")
            i+=1
            print(i)

print(time.ctime())
firstsTreatmentsOnFiles()
print(time.ctime())
