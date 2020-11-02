"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

def main():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
    longestCall(texts, calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longestCall(texts, calls):
    maxDuration = 0
    maxIndex = 0
    for item in range(0, len(calls)):
        if int(calls[item][3]) > maxDuration:
            maxDuration = int(calls[item][3])
            maxIndex = item
    print(calls[maxIndex][0] + " spent the longest time, " + str(maxDuration) + " seconds, on the phone during September 2016.")
        




if __name__ == "__main__":
    main()

