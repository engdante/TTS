import sys
import os
import io

def makeReplaceDict(inFile,outFile):
    file = io.open(inFile, mode="r", encoding="utf-8")
    char_list="" 
    for line in file:
        line = line.replace('\n','')
        for char in line:
            if char_list.find(char) == -1:
                char_list = char_list + char
    outFile = io.open(outFile, mode="w", encoding="utf-8")
    index = 1
    outFile.write("rep = {\n")
    for char in char_list:
        if index == len(char_list):
            outFile.write('\'' + char + '\'' + ':' + str(index+10) + '\n')
        else :
            outFile.write('\'' + char + '\'' + ':' + str(index+10) + ',\n')
        index += 1
    outFile.write("}")
    outFile.close()

def get_sounds(inFile,outFile):
    with io.open(inFile, mode="r", encoding="utf-8") as fIn , io.open(outFile, mode="w", encoding="utf-8") as fOut:
        for line in fIn:
            line = line.replace('\n','')
            line = line.lower()
            line = line.split("\t")
            if line[1].find(',') > 0:
                line[1] = line[1][:line[1].find(',')]
            line[1] = line[1][1:-1]
            fOut.write("{0}\n".format(line[1]))

   
inFile = "ipa-dict-master\data\en_US.txt"
outFile = "temp.txt"
repDict = "ReplaceDict.py"

if os.path.exists(outFile):
    os.remove(outFile)
if os.path.exists(repDict):
    os.remove(repDict)

get_sounds(inFile,outFile)
makeReplaceDict(outFile,repDict)
if os.path.exists(outFile):
    os.remove(outFile)