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
    numberofRecords(texts, calls)
    #countNumbers(texts, calls)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def numberofRecords(texts, calls):
    recordCount = 0
    for item in texts:
        for element in item:
            if isTelephoneNumber(element):
                recordCount += 1

    for item in calls:
        for element in item:
            if isTelephoneNumber(element):
                recordCount += 1
    records = str(recordCount)
    print("There are " + records + " different telephone numbers in the records.")
    return recordCount


def isTelephoneNumber(number):
    stringify = str(number)
    if isMobileNumber(stringify) or isFixedNumber(stringify) or isTeleMarketerNumber(stringify):
        return True
    else:            
        return False

def numberLength(stringify):
    if len(stringify) == 10 or len(stringify) == 11:
        return True
    else:
        return False

def isFixedNumber(number):
    if number.find("(") == 0:
        if number.find(")") == 4:
            number = number.replace("(", "", 1)
            number = number.replace(")", "", 1)
            if numberLength(number):
                return True
    
    return False

def isMobileNumber(number):
    mobilePrefixes = ['7', '8', '9']
    firstNumber = number[0:1]
    if firstNumber in mobilePrefixes:
        if numberLength(number):
            return True
    else:
        return False

def isTeleMarketerNumber(number):
    if number.startswith("140"):
        if numberLength(number):
            return True
    else:
        return False

def countAllRecords(texts, calls):
    allRecords = 0
    for item in texts:
        for element in item:
            allRecords += 1
    
    for item in calls:
        for element in item:
            allRecords += 1
    
    return allRecords


if __name__ == "__main__":
    main()


