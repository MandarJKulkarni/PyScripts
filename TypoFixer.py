#Prerequisite is to keep all your files; which you want to modify; under one directory
#Run the SpellChecker.py first to find out the typos from files and
#dump the corresponding suggestions in a text file

#Now you have to manually go through the text file created by SpellChecker script
#And select the suggestions that you want to take care of.
#For example if the mycsfiletypos.txt file can have below entries
#namespace : name space, names pace, namesake, nameplate, whitespace, nameless, 
#readonly : read only, readout, readopt, readably, readily, 
#Versoin : Version, Verso in, 
#alread : already, Alfred, lipread, allured, altered, 

#And if I want to fix only the versoin and alread typos, because the other 2 entries are valid,
#then you should fix the file to contain only below lines
#Versoin : Version
#alread : already
#if you find all the entries in typos.txt are invalid, remove all the entries and just keep the empty file.
#or delete the file
#Then this script PythonTypoFixer.py should be run on the same directory.

import os
import fileinput
import sys
import stat
import re
import threading

#TODO: Change this 'script' with better design using OOPS
def readTyposFile(typosFile, correctionsDict):
    for line in typosFile:
        typo,correction = line.split(" : ")
        correction=re.sub('[^A-Za-z]+','',correction)
        correctionsDict[typo] = correction
    return correctionsDict

def fixTheTypos(f2, filedata, correctionsDict):
    #lock =threading.Lock()
    #lock.acquire()
    for key,val in correctionsDict.items():
        filedata = filedata.replace(key, val)
    f2.write(filedata)
    f2.close()
    #lock.release()

if __name__ == "__main__":
    for root,dirs,files in os.walk("D:\\MyCode\\CSFiles"):
        for file in files:
            if file.endswith(".cs"):
                f1 = open(os.path.join(root, file),'r')
                typosFileName = file[:-3] +"typos.txt"
                if not os.path.isfile(os.path.join(root,typosFileName)):
                    continue
                typosFile = open(os.path.join(root,typosFileName),'r')
                correctionsDict=dict()
                t= threading.Thread(target=readTyposFile,args=(typosFile,correctionsDict))
                t.start()
                t.join()
                
                if len(correctionsDict) == 0:
                    continue
                filedata = f1.read()
                f1.close()
                
                f2=open(os.path.join(root,file),'w')
                t= threading.Thread(target=fixTheTypos,args=(f2,filedata, correctionsDict,))
                t.start()
