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
    unionSet = unionRegularNumbers(sentMessages, receivedMessages, incomingMessages, sendingSet)
    print("There are " + str(unionSet) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
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


def unionRegularNumbers(sendingTexts, receivingTexts, incomingCalls, sendingNumbers):
    regularNumbers = set()
    regularNumbers = sendingTexts.union(receivingTexts, incomingCalls, sendingNumbers)
    return len(regularNumbers)

def formatFixedNumber(number):
  newNumber = number.replace("(", "", 1)
  newNumber = newNumber.replace(")", "", 1)
  return newNumber


if __name__ == "__main__":
    main()


