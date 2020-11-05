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
    findMaxItem(getLongestCall(calls))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def getLongestCall(calls):
    callDuration = {}
    for item in range(0, len(calls)):
        if callDuration.get(calls[item][0]):
            callDuration[calls[item][0]] += int(calls[item][3])
        else:
            callDuration[calls[item][0]] = int(calls[item][3])
        if callDuration.get(calls[item][1]):
            callDuration[calls[item][1]] += int(calls[item][3])
        else:
            callDuration[calls[item][1]] = int(calls[item][3])
    return callDuration

def findMaxItem(callDurations):
    sorted_x = sorted(callDurations.items(), key=lambda kv: kv[1])
    callDurationLength = len(sorted_x) - 1
    print(sorted_x[callDurationLength][0] + " spent the longest time, " + str(sorted_x[callDurationLength][1]) + " seconds, on the phone during September 2016.")

if __name__ == "__main__":
    main()

