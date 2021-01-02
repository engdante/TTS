import sys
import io
import os
import Dictionary
import ReplaceDict

import matplotlib.pyplot as plt

import glob
import io

import time
start_time = time.time()


# input_file = sys.argv [1]
# output_file = sys.argv [2]
# print ("{0} / {1}".format(input_file,output_file))

def get_sounds_count(word):
    sounds_count = 1
    word_count = True
    while word_count:
        word = int(word / 100)
        # print (wordFromDictCount)
        if word == 0 :
            word_count = False
        else :
            sounds_count += 1
    return sounds_count

def split_sounds(word, count):
    sounds = []
    while count > 0:
        division = 100 ** (count - 1)
        sound = int (word / division)
        if sound > 0 :
            sounds.append(sound)
        else :
            return sounds
        count -= 1
        word = word - (sound * division)
    return sounds


rep_char = {'.' : '', ',' : '', '\'' : '', '\"' : '', '!' : '', '?' : ''}
sound_count = {}
for key, value  in ReplaceDict.rep.items():
    sound_count[str(value)]=0

import glob
fileNames = glob.glob('books\*.txt')
# print (fileNames)

for fileName in fileNames:
    file = io.open(fileName, mode="r", encoding="utf-8")
    for line in file: 
        for word in line.split():
            word = word.lower()
            for key, value  in rep_char.items():
                word = word.replace(key,value)
            wordSounds = Dictionary.dict.get(word)
            if wordSounds == None :
                continue
            wordSoundsCount = get_sounds_count(wordSounds)
            sounds = split_sounds(wordSounds, wordSoundsCount)
            for x in sounds:
                if str(x) in sound_count:
                    sound_count[str(x)] += 1
    # print (sound_count)
    sound_count_sort = dict(sorted(sound_count.items(), key=lambda item: item[1]))
    # print (sound_count_sort)

if os.path.exists("read_sounds.py"):
    os.remove("read_sounds.py")


outFile = io.open("read_sounds.py", mode="w", encoding="utf-8")
index = 1
outFile.write("read_sounds = {\n")
for key, val in sound_count_sort.items():
    outFile.write('\'' + str(key) + '\'' + ':' + str(val) + '\n')
    index += 1
outFile.write("}")
outFile.close()

plot_sound_count_sort = {}
for key, value in sound_count_sort.items():
    key = int(key)
    for dictKey, dictValue in ReplaceDict.rep.items():
        if key == dictValue:
            plot_sound_count_sort[dictKey] = value
# print (plot_sound_count_sort)

print("--- %s seconds ---" % (time.time() - start_time))

plt.bar(range(len(plot_sound_count_sort)), list(plot_sound_count_sort.values()), align='center')
plt.xticks(range(len(plot_sound_count_sort)), list(plot_sound_count_sort.keys()))
# plt.show()
filename = ("{0}.png".format(start_time))
plt.savefig(filename)


