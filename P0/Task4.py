"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def main():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        sentMessages = textSenderSet(texts)
        receivedMessages = textReceivedSet(texts)
        incomingMessages = incomingCallSet(calls)
        sendingSet = sendingNumbers(calls)
        unionSet = unionRegularNumbers(sentMessages, receivedMessages, incomingMessages)
        printSetTelemarketers(differences(unionSet, sendingSet))


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



def textSenderSet(texts):
    sentTexts = set()
    for text in texts:
        sentTexts.add(text[0])
    return sentTexts

def textReceivedSet(texts):
    receivedTexts = set()
    for text in texts:
        receivedTexts.add(text[1])
    return receivedTexts

def incomingCallSet(calls):
    incomingCalls = set()
    for call in calls:
        incomingCalls.add(formatFixedNumber(call[1]))
    return incomingCalls


def sendingNumbers(calls):
    sendingNumbers = set()
    for call in calls:
        sendingNumbers.add(formatFixedNumber(call[0]))
    return sendingNumbers


def unionRegularNumbers(sendingTexts, receivingTexts, incomingCalls):
    regularNumbers = set()
    regularNumbers = sendingTexts.union(receivingTexts, incomingCalls)
    return regularNumbers

def differences(regularNumbers, sendingNumbers):
    differenceSet = set()
    differenceSet = sendingNumbers - regularNumbers
    return sorted(differenceSet)

def printSetTelemarketers(suspectList):
    print("These numbers could be telemarketers:")
    for number in suspectList:
        print(number)


def numberLength(stringify):
    stringify = str(stringify)
    if len(stringify) == 10 or len(stringify) == 11:
        return True
    else:
        return False

def formatFixedNumber(number):
  newNumber = number.replace("(", "", 1)
  newNumber = newNumber.replace(")", "", 1)
  return newNumber


def isTeleMarketerNumber(number):
    if number.startswith("140"):
        if numberLength(number):
            return True
    else:
        return False



if __name__ == "__main__":
    main()