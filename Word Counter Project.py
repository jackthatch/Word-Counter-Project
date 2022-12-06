import string
import matplotlib.pyplot as plt
import numpy as np


def fileHandling():
    file = open("essay.txt", encoding="utf8")
    text = file.read()
    text = text.lower()
    text = text.translate(('', '', string.punctuation))
    text = text.split()
    
    return text


def createDictionary(text):
    wordDict = {}
    for ele in text:
        if ele not in wordDict:             ##Add item to dictionary if it doesn't exist
            wordDict.update({ele : 1})
        else:
            wordDict[ele] += 1          ##Increasing counter of item in list 
        
    return wordDict


def keyInfo(x):             ##Passing in unsorted dictionary
    for ele in x.copy():
        if x[ele] == 0:         ##Getting rid of items that appear once
            del x[ele]
    if len(ele) == 1:
        del x[ele]
    
    return x

def sortDict(x):           ##Passing in our dictionary of key values
    sortedDict = {}
    sortedKeys = sorted(x, key=x.get, reverse=True)

    for ele in sortedKeys:
        sortedDict[ele] = x[ele]
    

    return (sortedDict)


def topWords(x):            ##Create new dictionary of top 25 terms in the dictionary, passing in our sorted dictionary keys

    topWordsList = list(x.items())
    newTopWordsList = []
    i = 0
    while len(newTopWordsList) < 25:
        newTopWordsList.append(topWordsList[i])
        i += 1
        

    return newTopWordsList


def plotGraph(list):
    x_val = [x[0] for x in list]
    y_val = [x[1] for x in list]

    plt.bar(x_val, y_val)
    plt.title("Word Frequency", loc = "left")
    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.grid()
    plt.show()





newDictionary = createDictionary(fileHandling())

keyInfoDict = keyInfo(newDictionary)

sortedKeyDict = sortDict(keyInfoDict)

topWordsList = topWords(sortedKeyDict)

print(topWordsList)

plotGraph(topWordsList)


## Possbile improvements: display what % a take up in the entire document
## Take in more than one file
## Allow users to choose how many key words to display




