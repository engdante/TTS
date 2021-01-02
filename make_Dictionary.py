import sys
import os
import io

import ReplaceDict

def replace_sounds(inFile,outFile,replace_dic):
    with io.open(inFile, mode="r", encoding="utf-8") as fIn , io.open(outFile, mode="w", encoding="utf-8") as fOut:
        fOut.write("dict = {\n")
        line_total_count = 0
        line_count = 0
        for line in fIn:
            line_total_count += 1
        print ("{0} line".format(line_total_count))
        fIn.seek(0, 0)
        for line in fIn:
            line_count += 1
            line = line.replace('\n','')
            line = line.lower()
            line = line.split("\t")
            if line[1].find(',') > 0:
                line[1] = line[1][:line[1].find(',')]
            line[1] = line[1][1:-1]
            # fOut.write("{0}\n".format(line[1]))
            for f_key, f_value in replace_dic.items():
                if f_key in line[1]:
                    line[1] = line[1].replace(str(f_key), str(f_value))
            line[0] = line[0].replace('\'', '^')
            line[0] = '\'' + str(line[0]) + '\''
            # print ("{0} : {1}".format(line[0], line[1]))
            if line_count == line_total_count:
                fOut.write("\t{0} : {1}\n".format(line[0], line[1]))
            else : 
                fOut.write("\t{0} : {1},\n".format(line[0], line[1]))
        fOut.write("}")

   
inFile = "ipa-dict-master\data\en_US.txt"
outFile = "Dictionary.py"
replace_dic = ReplaceDict.rep


if os.path.exists(outFile):
  os.remove(outFile)

replace_sounds(inFile,outFile,replace_dic)