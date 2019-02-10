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
        for i in range(len(words) - 3):
            reference = words[i] + words[i+1] + words[i+2] + words[i+3]
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
    n = 50000
    abstracts = getData()
    dataset = parseArray(abstracts, n)
    training_data = createHashMap(dataset)

    starting_string = "this study "
    next_string = starting_string
    final_string = starting_string

    while next_string != None:
        next_string = getNextString(next_string, training_data)
        if next_string != None:
            final_string += next_string
    print(final_string)

main()
