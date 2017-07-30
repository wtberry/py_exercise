'''
solution using simple for loop and str methods
'''
fi = open('data/113809of.fic')

count = 0
for line in fi:
    if line.count('a') == 2 and 'e' not in line:
        word = line.strip('\n')
        print(word)
        count +=1
print('total number of the words are', count)
fi.close()

print(3*'\n')
print('second solution from here: \n')
'''
using csv module to strip the new line
'''

import csv
fl = open('data/113809of.fic', newline='')
word_l = []
c_reader = csv.reader(fl)
for wordlist in c_reader:
    word = wordlist[0]  # list to string of word
    if word.count('a') == 2 and word.count('e') == 0:
        print(word)
        word_l.append(word)

print('list of the words which includes 2 \'a\'s and no \'e\' is\n', word_l)
print('number of the words are', len(word_l))
fl.close()
