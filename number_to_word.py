import csv

number_to_word_file = []
with open("number_to_word.csv") as number_to_word_raw:
    temp = csv.reader(number_to_word_raw)
    for row in temp:
        number_to_word_file.append(row)

def num_to_word(num):
    for line in number_to_word_file:
        if line[0] == str(num):
            return line[1]
    try:
        return str(num)
    except:
        return num