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
    unionSet = getNumbers(calls, texts)
    print("There are " + str(unionSet) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getNumbers(texts, calls):
    uniqueNumbers = set()
    for item in texts:
        uniqueNumbers.add(item[0])
        uniqueNumbers.add(item[1])
    for item in calls:
        uniqueNumbers.add(item[0])
        uniqueNumbers.add(item[1])
    return len(uniqueNumbers)

if __name__ == "__main__":
    main()


