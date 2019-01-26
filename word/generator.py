import oxfordAPILib
import csv

word_dict = {}
with open('french-word-list-total.csv', 'r') as word_list:
    csv_reader = csv.reader(word_list, delimiter=',')
    n = 0
    for row in csv_reader:
        col_list = row[0].split(';')
        word_n = col_list[0]
        word = col_list[1]
        freq = col_list[2]
        word_dict[word_n] = [word, freq]

print(word_dict)

def getWord():
    pass