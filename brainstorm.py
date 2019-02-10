import pandas as pd

def cleanData(array):
    new_list = []
    for i in array:
        if type(i) != type(1.0): # Modern problems require modern solutions
            new_list.append(i)
    else:
        return new_list

def parseArray(array):
    master_list = []
    sub_list = []

    for abstract in array[:10]:
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
            reference = [words[i], words[i+1], words[i+2], words[i+3]]
            if reference not in dict.keys():
                dict[reference] = 1
            else:
                dict[reference] += 1

    return dict

def main():
    df_pub = pd.read_csv('publications.csv', delimiter=',')
    list_pub_abstracts = list(df_pub.abstract)
    abstracts = cleanData(list_pub_abstracts)
    dataset = (parseArray(abstracts))
    dictionary = createHashMap(dataset)

    #print(dataset)
    #print(dictionary)

main()
