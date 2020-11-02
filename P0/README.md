# Reflection on this project

## Task 0

For Task 0, I identified the first and last records using python's slicing. 

The Big O for this would be linear O(n), because the part of my code which would grow the
most is my len() function call, which would grow linearly as items are added to the dataset. 

## Task 1 

For Task 1, I used multiple nested for loops to identify different telephone
numbers in the phone records and to check for certain conditions. 

The efficiency/Big O for this is 0(n^2), which isn't ideal. 

While working on this task, I considered several different ways to correctly identify a
phone number based on different criteria -- we were given several different parameters to consider,
such as mobile numbers, telemarketer numbers, and landlines. 

I found this task challenging as I practiced clarifying requirements and decomposing the function.

## Task 2 

For Task 2, I identified the phone record with the longest duration. 

My solution for this is O(n) since my code will run longer in a linear fashion (3x slower) as there
are three additional lines that would need to be processed and run with an additional item
added to the dataset. 