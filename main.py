import pandas as pd
import random

def parseArray(array, n):
    master_list = []
    sub_list = []

    for abstract in array[:n]:
        abstract += ' '
        word = ''

        for letter in abstract:
            letter = letter.lower()

            if letter != ' ':
                word += letter

            elif letter == ' ' or letter:
                word += ' '
                sub_list.append(word)
                word = ''

        master_list.append(sub_list)
        sub_list = []

    return master_list

def createHashMap(array):
    dict = {}

    for words in array:
        for i in range(len(words) - 5):
            reference = words[i] + words[i+1] + words[i+2] + words[i+3] + words[i+4] + words[i+5]
            if reference not in dict.keys():
                dict[reference] = 1
            else:
                dict[reference] += 1

    return dict

def findKeys(string, dict):
    keys = []
    for i in dict.keys():
        if i[:len(string)] == string:
            keys.append(i)

    return keys

def getRandomNumber(array, dict):
    accum = 0
    for i in array:
        accum += dict[i]

    return random.randrange(1, accum + 1)

def getNextString(string, dict):
    keys = findKeys(string, dict)
    if keys == []:
        return None
    random_no = getRandomNumber(keys, dict)
    for i in keys:
        random_no -= dict[i]
        if random_no <= 0:
            return i[len(string):]

def getData():
    df_pub = pd.read_csv('publications.csv', delimiter=',')
    list_pub_abstracts = list(df_pub.abstract)
    abstracts = cleanData(list_pub_abstracts)

    return abstracts

def cleanData(array):
    new_list = []
    for i in array:
        if type(i) != type(1.0): # Modern problems require modern solutions
            new_list.append(i)
    else:
        return new_list

def main():
    #abstracts = ["The quick brown fox jumps over the lazy dog.", "The quick lazy dog jumps over the brown fox.", "The quick lazy dog jumps over the brown fox."]
    n = 10000
    abstracts = getData()
    data_array = parseArray(abstracts, n)
    data_dict = createHashMap(data_array)

    starting_string = "this study "
    next_string = starting_string

    output = open("output.txt", 'w')
    while next_string != None:
        output.write(next_string)
        next_string = getNextString(next_string, data_dict)
        if next_string == None:
            break

    output.close()

main()
