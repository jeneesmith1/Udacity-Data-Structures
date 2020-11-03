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

    numbers = getSendingNumbers(calls)
    areaCodes = getAreaCodesCalledByBangalore(numbers)
    printCallsbyBangalore(areaCodes)
    printPercentage(percentage(numbers))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

approach -- binarySearch to go through the numbers will be more efficient than 
"""


def getSendingNumbers(calls):
  # takes the calls and returns the sorted sending numbers
  numbers = []
  sendingNumbers = []
  for item in range(0, len(calls)):
    numbers.append([formatFixedNumber(calls[item][0]), formatFixedNumber(calls[item][1])])
  return sorted(numbers)



def searchBangaloreNumbers(numbers):
  # takes the sorted sending numbers so that can start search for Bangalore numbers
  bangaloreNumber = '080'
  sendingNumbers = []
  for number in numbers:
    sendingNumbers.append(number[0][0:3])

  bangaloreNumberStartIndex = binarySearchStartIndex(sendingNumbers, 0, len(sendingNumbers)-1, bangaloreNumber)
  bangaloreNumberEndIndex = binarySearchEndIndex(sendingNumbers, 0, len(sendingNumbers)-1, bangaloreNumber)
  return [bangaloreNumberStartIndex, bangaloreNumberEndIndex]
  

def countCallsfromBangalore(startIndex, endIndex):
  return (endIndex - startIndex)

def countReceivedCalls(numbers):
  count = 0
  callRange = searchBangaloreNumbers(numbers)
  for number in range(callRange[0], callRange[1]):
    receivedNumber = formatFixedNumber(numbers[number][1])
    if receivedNumber.startswith('080'):
      count += 1
  return count

def percentage(numbers):
  callRange = searchBangaloreNumbers(numbers)
  totalCalls = countCallsfromBangalore(callRange[0], callRange[1])
  received = countReceivedCalls(numbers)
  answer = received / totalCalls * 100
  return answer

def printPercentage(percentage):
  print("{:.2f}".format(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

def getAreaCodesCalledByBangalore(numbers):
  #gets the area codes for numbers called
  callRange = searchBangaloreNumbers(numbers)
  areaCodes = []
  for number in range(callRange[0], callRange[1]):
    areaCodes = getFullListAreaCodes(callRange[0], callRange[1], numbers)
  return sorted(areaCodes)


def printCallsbyBangalore(areaCodes):
  #prints the total numbers of people called
  print("The numbers called by people in Bangalore have codes:")
  for code in areaCodes:
    print(code)


def getFullListAreaCodes(startIndex, endIndex, calls):
  #gets the area codes
  areaCodes = []
  for number in range(startIndex, endIndex):
    receivedNumber = formatFixedNumber(calls[number][1])
    if isMobileNumber(receivedNumber):
      if receivedNumber[0:4] not in areaCodes:
        areaCodes.append(receivedNumber[0:4])
    else:
      if receivedNumber[0:3] not in areaCodes:
        areaCodes.append(receivedNumber[0:3])
  return areaCodes


def binarySearchStartIndex(array, low, high, searchItem):
  #gets the first index for the search term in the list passed into it
  startIndex = -1
  return binarySearchStartHelper(array, low, high, searchItem, startIndex)


def binarySearchStartHelper(array, low, high, searchItem, startIndex):
  if low >= high:
    return startIndex
  else:
    mid = (high - low) // 2 + low
    if array[mid] > searchItem:
      return binarySearchStartHelper(array, low, mid - 1, searchItem, startIndex)
    elif array[mid] == searchItem:
      startIndex = mid
      high = mid - 1
      return binarySearchStartHelper(array, low, mid - 1, searchItem, mid)
    else:
      return binarySearchStartHelper(array, mid + 1, high, searchItem, mid)



def binarySearchEndIndex(array, low, high, searchItem):
  #gets the last index for the search term in the list passed into it
  endIndex = -1
  return binarySearchEndHelper(array, low, high, searchItem, endIndex)
  

def binarySearchEndHelper(array, low, high, searchItem, endIndex):
  if low >= high:
    return endIndex
  else:
    mid = (high - low) // 2 + low
    if array[mid] > searchItem:
      return binarySearchEndHelper(array, low, mid - 1, searchItem, endIndex)
    elif array[mid] == searchItem:
      return binarySearchEndHelper(array, mid + 1, high, searchItem, mid)
    else:
      return binarySearchEndHelper(array, mid + 1, high, searchItem, endIndex)


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


def isMobileNumber(number):
    mobilePrefixes = ['7', '8', '9']
    firstNumber = number[0:1]
    if firstNumber in mobilePrefixes:
        if numberLength(number):
            return True
    else:
        return False





if __name__ == "__main__":
    main()