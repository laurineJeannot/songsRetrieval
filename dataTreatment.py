import os
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

def getMostUsedWords(song,n):
    #TODO list the most used words in the song
    return []
    
def generateLexicalFields(word,n):
    #TODO take a word and generates n hypernyms with wordnet
    hypernymList = []


    return hypernymList

def writeResults():
    #TODO write all the results in a single txt file
    open("finalData.txt","w")



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
    for filename in corpus_filenames:
        songListWithWords = getListOfSongsAndWords(directory+filename)
        n = 5
        for s in songListWithWords :
            song = Song(s[0],s[1])
            print(song)
            words = getMostUsedWords(s,n)
            for w in words :
               generateLexicalFields(w,n)

    """
    ============================================================
    Get artist and Title
    ============================================================
    """

    """
    ============================================================
    Write the results
    ============================================================
    """


    writeResults()

firstsTreatmentsOnFiles()
