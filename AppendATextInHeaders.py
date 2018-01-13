#Prerequisite: Dump the list of headers that you want to modify in a text file
#I wanted to append Microsoft's banned.h in every header of our source code
#I had to append the #include at the end of the file and this script saved me a lot of time.
import os
headerList = open("headersToModify.txt","w")
for root,dirs,files in os.walk("."):
    for file in files:
        if file.endswith(".h") or file.endswith(".hh") :
            if os.name == "nt":
                headerList.write(root+"\\"+file+"\n")
                os.chmod(root+"\\"+file, 511)
                writefile = open(root+"\\"+file, "a")
                writefile.write("\n#ifndef _INC_BANNED \n#include \"banned.h\"\n#endif\n")
                writefile.close()
            if os.name == "posix":
                headerList.write(root+"/"+file+"\n")
                os.chmod(root+"/"+file, 511)
                writefile = open(root+"/"+file, "a")
                writefile.write("\n#ifndef _INC_BANNED \n#include \"banned.h\"\n#endif\n")
                writefile.close()
