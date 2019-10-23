#implement function that plots every day with the number of messages

"""functions:   deleteMetaData()
                filterMetaData()
                daysMostChatted()
                hoursMostChatted()
                personMostChatted()
                averageWordsPerMessage()
                findNumberOfCharacters()
                findNumberOfWords()
                findNumberOfMessages()
                findMostUsedWords()
                findMostUsedLetters()
                findMostUsedEmojis()
"""

import re
import collections
import sys
import emoji
import matplotlib.pyplot as plt
import numpy as np

chat = open("chat.txt", "r")
chat2 = open("chat2.txt", "w+")
output = open("output.txt", "w+")

metaData = re.compile("\[\d\d\.\d\d\.\d\d,\s\d\d:\d\d:\d\d\]\s.+?:")
metaDataDayTime = re.compile("\\d\d\.\d\d\.\d\d")
metaDataHourTime = re.compile("\\d\d:\d\d:\d\d")
metaDataName = re.compile("\]\s.+?:")

namesList = []

def filterMetaData():
    
    #filters the metaData and finds the name of users
    #takes global vars nameOne and nameTwo and changes it
    
    global namesList
    chat = open("chat.txt").readlines()
    x = 0
    previousMatch = ""
    matchUserName = re.compile("]\s.+?:")
    
    for i in chat:
        matchOne = re.findall(metaData, i)
        for i2 in matchOne:
            matchTwo = re.findall(metaDataName, i2)
            for i3 in matchTwo:
                if x == 0:
                    name = i3
                    name = name[2:-1]
                    namesList.append(name)
                    previousMatch = i3[2:-1]
                    x += 1
                elif i3[2:-1] != previousMatch and i3[2:-1] not in namesList:
                    name = i3
                    name = name[2:-1]
                    namesList.append(name)
                    previousMatch = i3[2:-1]
                    x += 1
    
    for i in namesList:
        output.write(i + "\n")
        
    return namesList


def deleteMetaData():
    # deletes the meta data and writes a new file "chat2.txt"
    
    chat = open("chat.txt", "r")
    chat2 = open("chat2.txt", "w+")
    
    for i in chat:
        chat2.write(re.sub(metaData, "", i))
        

def firstLastMessage():
    #Finds the first and last message sent
    
    lengthFirstMeta = len(namesList[0]) + 23
        
    message = findNumberOfMessages()
    firstMessage = ""
    lastMessage = ""
    counter = 0
    previousCounter = 0
        
    for i in chat:
        
        if counter == 1:
            firstMessage = namesList[0] + "$" + i[1:19] + "$" + i[lengthFirstMeta:-2]
            
        elif counter >= previousCounter:
            for names in namesList:
                if names in i:
                    lastName = names
                    lengthSecondMeta = len(lastName) + 23
                    lastMessage = lastName + "$" + i[1:19] + "$" + i[lengthSecondMeta:-2]
                    
        
        previousCounter = counter
        counter += 1
    
    output.write(firstMessage + "\n" + lastMessage + "\n")
        
    return firstMessage
        

def daysMostChatted():
    #finds the days with the most messages
    
    numberOfMatches = 0
    previousMatch = "20.07.18"
    listOfDays = []
    match = re.findall(metaDataDayTime, open("chat.txt").read().lower())
    
    for i in match:
        
        if i == previousMatch:
            numberOfMatches += 1
        else:
            newListElement = (str(numberOfMatches), previousMatch)
            listOfDays.append(newListElement)
            previousMatch = i
            numberOfMatches = 1
                
    highestNumber = 0
    previousNumber = 0
    day = ""
    listOfHighestDays = []                     
    
    for matches in listOfDays:
        if int(matches[0]) > previousNumber:
            highestNumber = int(matches[0])
            previousNumber = int(matches[0])
        
    x = highestNumber
    
    while len(listOfHighestDays) <= 10:
        for matches in listOfDays:
            if int(matches[0]) == x:
                listOfHighestDays.append(matches)
        x -= 1
    
    output.write(str(listOfHighestDays) + "\n")
    return listOfHighestDays

def hoursMostChatted():
    # finds out on which hours how many messages were sent in total
    
    zeroHours, oneHours, twoHours, threeHours, fourHours, fiveHours, sixHours, sevenHours, eightHours, nineHours, tenHours, elevenHours, twelveHours, thirteenHours, fourteenHours, fifteenHours, sixteenHours, seventeenHours, eighteenHours, nineteenHours, twentyHours, twentyOneHours, twentyTwoHours, twentyThreeHours = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    
    metaDataHoursTimeAlpha = re.compile("\d\d:\d\d:\d\d\]")
    metaDataHours = re.compile("\d\d")
    matchList = []
    
    match = re.findall(metaDataHoursTimeAlpha, open("chat.txt").read().lower())
    for i in match:
        matchList.append(i)
    
    for i in matchList:
        if i[:2] == "00":
            zeroHours += 1
        elif i[:2] == "01":
            oneHours += 1
        elif i[:2] == "02":
            twoHours += 1
        elif i[:2] == "03":
            threeHours += 1
        elif i[:2] == "04":
            fourHours += 1
        elif i[:2] == "05":
            fiveHours += 1
        elif i[:2] == "06":
            sixHours += 1
        elif i[:2] == "07":
            sevenHours += 1
        elif i[:2] == "08":
            eightHours += 1
        elif i[:2] == "09":
            nineHours += 1
        elif i[:2] == "10":
            tenHours += 1
        elif i[:2] == "11":
            elevenHours += 1
        elif i[:2] == "12":
            twelveHours += 1
        elif i[:2] == "13":
            thirteenHours += 1
        elif i[:2] == "14":
            fourteenHours += 1
        elif i[:2] == "15":
            fifteenHours += 1
        elif i[:2] == "16":
            sixteenHours += 1
        elif i[:2] == "17":
            seventeenHours += 1
        elif i[:2] == "18":
            eighteenHours += 1
        elif i[:2] == "19":
            nineteenHours += 1
        elif i[:2] == "20":
            twentyHours += 1
        elif i[:2] == "21":
            twentyOneHours += 1
        elif i[:2] == "22":
            twentyTwoHours += 1
        elif i[:2] == "23":
            twentyThreeHours += 1
    
    output.write(str(zeroHours) + "$" + str(twoHours) + "$" + str(threeHours) + "$" + str(fourHours) + "$" + str(fiveHours) + "$" + str(sixHours) + "$" + str(sevenHours) + "$" + str(eightHours) + "$" + str(nineHours) + "$" + str(tenHours) + "$" + str(elevenHours) + "$" + str(twelveHours) + "$" + str(thirteenHours) + "$" + str(fourteenHours) + "$" + str(fifteenHours) + "$" + str(sixteenHours) + "$" + str(seventeenHours) + "$" + str(eighteenHours) + "$" + str(nineteenHours) + "$" + str(twentyHours) + "$" + str(twentyOneHours) + "$" + str(twentyTwoHours) + "$" + str(twentyThreeHours) + "\n")

def personMostChatted():
    #finds the amount of messages per person
    
    chat = open("chat.txt", "r")
    
    messagesList = []
    
    for i in chat:
        for names in namesList:
            if names in i:
                if names not in messagesList:
                    messagesList += (names, int(1))
                else:
                    for elements in messagesList:
                        if names in elements:
                            elements[1] += 1
    
    print(messagesList)
    
    return 0
    
    
def averageWordsPerMessage():
    # finds the average words per message
    
    words = findNumberOfWords()
    messages = findNumberOfMessages()
    
    averageWord = (words/messages)
    
    output.write(str(averageWord) + "\n")
    
    return averageWord

#def averageCharactersPerMessage():

    
def findNumberOfCharacters():
    # finds the total number of Characters
    
    counter = 0
    chat = open("chat2.txt").read().lower()
    
    for i in chat:
        counter += 1
        
    output.write(str(counter) + "\n")
    
    return counter

def findNumberOfWords():
    # finds the total number of Words
    
    wordCounter = 0
    wordPattern = re.compile("\w+")
    matches = re.findall(wordPattern, open("chat2.txt").read().lower())
    
    for i in matches:
        wordCounter += 1
        
    output.write(str(wordCounter) + "\n")
    
    return float(wordCounter)

def findNumberOfMessages():
    # finds the total number of Messages
    
    numberOfMessages = 0
    matches = re.findall(metaData, open("chat.txt").read().lower())
    
    for i in matches:
        numberOfMessages += 1
        
    output.write(str(numberOfMessages) + "\n")
    
    return numberOfMessages

def findMostUsedWords():
    #returns top 20 most used words
    
    words = re.findall(r"\w+", open("chat2.txt").read().lower())
    mostCommon = collections.Counter(words).most_common(22)
    
    output.write(str(mostCommon) + "\n")
    
    return mostCommon

def findMostUsedLetters():
    #returns top 10 most used letters
    
    letters = re.findall(r"\w", open("chat2.txt").read().lower())
    mostCommon = collections.Counter(letters).most_common(10)
    
    output.write(str(mostCommon) + "\n")
    
    return mostCommon

def findMostUsedEmojis():
    #returns top 10 most used emojis
    
    chat = open("chat2.txt").read().lower()
    emojiCounter = 0
    
    listOfEmojis = emoji.UNICODE_EMOJI
    usedEmojis = []
    
    for i in chat:
        for i2 in i:
            if i2 in listOfEmojis:
                emojiCounter += 1
                if i2 not in usedEmojis:
                    usedEmojis += i2, 1
                else:
                    index = usedEmojis.index(i2)
                    usedEmojis[index + 1] += 1
    
    listCounter = 1
    topEmojis = []
    previousNumber = 0
    
    while len(usedEmojis) >=listCounter:
        if usedEmojis[listCounter] >= previousNumber:
            topEmojis = []
            topEmojis += usedEmojis[listCounter - 1], usedEmojis[listCounter]
            previousNumber = usedEmojis[listCounter]
        listCounter += 2
    
    x = topEmojis[1] - 1
    listCounter = 1
    
    while len(topEmojis) < 30:
        for i in usedEmojis:
            if i == x:
                index = usedEmojis.index(i)
                topEmojis += usedEmojis[index - 1], usedEmojis[index]
        x -= 1
    
    output.write(str(emojiCounter) + "\n" + str(topEmojis))
                    
    return emojiCounter, topEmojis

def daysTotal():
    #plots the number Of messages to its days
    
    match = re.findall(metaDataDayTime, open("chat.txt").read().lower())
    daysList = []
    numbersList = []
    previousDay = ""
    
    for i in match:
        if i != previousDay:
            daysList.append(i)
            numbersList.append(1)
            previousDay = i
        else:
            numbersList[-1] += 1
    
    numberOfDays = len(daysList)
    counter = numberOfDays/10
    
    plt.title = "Number Of Messages Per Day"
    plt.plot(daysList, numbersList, "b-", label="messages")
    plt.xlabel("Days")
    plt.ylabel("Number Of Messages")
    plt.xticks(daysList[::int(counter)], rotation=90)
    plt.legend()
    plt.savefig("messagePlot.svg", bbox_inches = "tight", transparent = True, dpi = 100, format="svg")
    
    return 0

def writeOutData():
    output = open("output.txt", "w+")


# setup for automatic program
if __name__ == "__main__":
    
    filterMetaData()
    deleteMetaData()
    firstLastMessage()
    daysMostChatted()
    hoursMostChatted()
    #personMostChatted()
    findNumberOfCharacters()
    findNumberOfWords()
    findNumberOfMessages()
    averageWordsPerMessage()
    findMostUsedWords()
    findMostUsedLetters()
    findMostUsedEmojis()
    daysTotal()
    
    
chat.close()
chat2.close()
output.close()

# end of program