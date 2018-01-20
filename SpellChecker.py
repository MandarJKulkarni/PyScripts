#prerequisite: You need to have enchant module installed
#Currently it searches all comments in C# files in a dictionary
#Suggestions for typos are dumped in a text file

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
            if not enUSDict.check(subword) and subword not in suggestionsDict.keys():
                typosFile.write(subword+' : ')
                suggestions = enUSDict.suggest(subword)
                suggestionsDict[subword] = suggestions
                for suggestion in suggestions:
                    typosFile.write(suggestion +", ")
                typosFile.write("\n")

    elif (isinstance(subWords,str)):
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
                typosFileName = file[:-3] +"typos.txt"
                typosFile = open(os.path.join(root,typosFileName),'w')
                suggestionsDict = dict()
                for line in f1:
                    line = line.strip()
                    if line.startswith("////") or line.startswith("#"):
                        words = line.split()
                        for word in words:
                            word = word.replace("#","")
                            subWords = re.findall('[A-Z][a-z]*',word)
                            if(len(subWords) > 0):
                                checkWordInDict(subWords,suggestionsDict,typosFile)
                            else:
                                checkWordInDict(word, suggestionsDict,typosFile)
                            #sys.stdout.write(word)
                            #sys.stdout.write(" ")
                        
               #         sys.stdout.write("\n")
               #         sys.stdout.flush()
                 
                    