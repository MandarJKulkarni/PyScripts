#prerequisite: You need to have enchant module installed
#Currently searches for all c# files in a directory
#Suggestions for typos are dumped in a text file with the name derived from C# file name

import enchant
import wx
import os
import fileinput
import sys
import stat
import re

enUSDict = enchant.Dict("en_US")

def checkWordInDict(subWords, suggestionsDict,typosFile):
    if(isinstance(subWords, list)):
        for subword in subWords:
            #remove non-alpha characters like ; , : - etc.
            nonAlphaCharacters = re.compile('[^a-zA-Z]+')
            subword = nonAlphaCharacters.sub('',subword)
            
            if len(subword)>0 and not enUSDict.check(subword) and subword not in suggestionsDict.keys():
                typosFile.write(subword+' : ')
                suggestions = enUSDict.suggest(subword)
                suggestionsDict[subword] = suggestions
                for suggestion in suggestions:
                    typosFile.write(suggestion +", ")
                typosFile.write("\n")

    elif (isinstance(subWords,str)):
        #remove non-alpha characters like ; , : - etc.
        nonAlphaCharacters = re.compile('[^a-zA-Z]+')
        subWords = nonAlphaCharacters.sub('',subWords)

        if not enUSDict.check(subWords) and subWords not in suggestionsDict.keys():
            typosFile.write(subWords+' : ')
            suggestions = enUSDict.suggest(subWords)
            suggestionsDict[subWords] = suggestions
            for suggestion in suggestions:
                typosFile.write(suggestion +", ")
            typosFile.write("\n")

if __name__ == "__main__":
    for root,dirs,files in os.walk("D:\\MyCode\\CSFiles"):
        for file in files:
            if file.endswith(".cs"):
                f1 = open(os.path.join(root, file),'r')
                typosFileName = file +"typos.txt"
                typosFile = open(os.path.join(root,typosFileName),'w')
                
                suggestionsDict = dict()
                for line in f1:
                    line = line.strip()
                    words = line.split()
                    for word in words:
                        word = word.replace("#","")
                        if not re.match(('[A-Za-z]'),word):
                            continue
                        #Find words starting with capital letters
                        subWords = re.findall('[A-Z][a-z]*',word)
                        #Find words starting with small letters
                        subWords + re.findall('[a-z][A-Z]*',word)
                        if(len(subWords) > 0):
                            checkWordInDict(subWords,suggestionsDict,typosFile)
                        else:
                            checkWordInDict(word, suggestionsDict,typosFile)
                    
