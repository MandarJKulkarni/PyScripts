#Prerequisite is to keep all your files which you want to modify under one directory
#The command line argument will change the string in all files of a certain extension
#If the command line argument is revert, it will revert the change

#My purpose was to change the platform toolset of all vcxproj files from v100 to v140.
#The option Update would upgrade from v100 to v140.
#The option revert would change the vcxproj files back to v100.

#Files extension to search for: argv[1]
#argv[2] : update -> replace argv[3] with argv[4]
#argv[2] : revert -> replace argv[4] with argv[3]
#Text to look for: argv[3]
#Text to replace with: argv[4]

import os
import fileinput
import sys
import stat

def changeFileContent(root, file, newdata):
    os.chmod( os.path.join(root, file), stat.S_IWRITE )
    f2 = open(os.path.join(root, file),'w')
    f2.write(newdata)
    f2.close()

if __name__ == "__main__":
    update =False
    revert=False
    if (len(sys.argv)>2 and sys.argv[2] == 'update'):
        update=True
    elif(len(sys.argv)>2 and sys.argv[2]=='revert'):
        revert=True

    f=open("myvcxprojs","w")
    #ToDo: Get the directory as input from user
    for root,dirs,files in os.walk("D:\\MY_CODE"):
        for file in files:
            if file.endswith(sys.argv[1]):
                #TODO: Instead of writing all file names in one file, put them in a separate file
                f.write(os.path.join(root, file) + '\n')

                f1 = open(os.path.join(root, file),'r')
                filedata = f1.read()
                f1.close()
                if(sys.argv[3] in filedata):
                    if(update):
                        newdata = filedata.replace(sys.argv[3], sys.argv[4])
                        changeFileContent(root,file,newdata)
                elif(sys.argv[4] in filedata):
                    if(revert):
                        newdata = filedata.replace(sys.argv[4], sys.argv[3])
                        changeFileContent(root,file,newdata)
    f.close()
