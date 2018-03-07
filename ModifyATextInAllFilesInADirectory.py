#Prerequisite is to keep all your files which you want to modify under one directory
#The command line argument will change the string in all files of a certain extension
#If the command line argument is revert, it will revert the change

#My purpose was to change the platform toolset of all vcxproj files from v100 to v140.
#The option Update would upgrade from v100 to v140.
#The option revert would change the vcxproj files back to v100.

#Files extension to search for: .vcxproj
#Text to look for: <PlatformToolset>v100</PlatformToolset>
#Text to replace with: <PlatformToolset>v140</PlatformToolset>

#ToDo: Need to make the above 3 options as command line arguments

import os
import fileinput
import sys
import stat
upgradeTo140 =False
revertTo100=False
if (len(sys.argv)>1 and sys.argv[1] == 'Update'):
    upgradeTo140=True
elif(len(sys.argv)>1 and sys.argv[1]=='revert'):
    revertTo100=True

f=open("myvcxprojs","w")
for root,dirs,files in os.walk("D:\\MY_CODE"):
    for file in files:
        if file.endswith(".vcxproj"):
            f.write(os.path.join(root, file) + '\n')
           # from shutil import copyfile
            f1 = open(os.path.join(root, file),'r')
            filedata = f1.read()
            f1.close()
            if("<PlatformToolset>v100</PlatformToolset>" in filedata):
                if(upgradeTo140):
                    newdata = filedata.replace("<PlatformToolset>v100</PlatformToolset>", "<PlatformToolset>v140</PlatformToolset>")
                else:
                    newdata =filedata
            elif("<PlatformToolset>v140</PlatformToolset>" in filedata):
                if(revertTo100):
                    newdata = filedata.replace("<PlatformToolset>v140</PlatformToolset>", "<PlatformToolset>v100</PlatformToolset>")
                else:
                    newdata = filedata
            else:
                newdata = filedata.replace("<CharacterSet>MultiByte</CharacterSet>", "<PlatformToolset>v140</PlatformToolset>\n<CharacterSet>MultiByte</CharacterSet>")
                newdata = newdata.replace("<UseOfMfc>false</UseOfMfc>", "<UseOfMfc>false</UseOfMfc>\n<PlatformToolset>v140</PlatformToolset>")
            os.chmod( os.path.join(root, file), stat.S_IWRITE )
            f2 = open(os.path.join(root, file),'w')
            f2.write(newdata)
            f2.close()
f.close()
