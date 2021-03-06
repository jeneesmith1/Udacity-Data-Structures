# Reflection on this project

## Task 0

For Task 0, I identified the first and last records using python's slicing. 

The Big O for this would be linear O(n), because the part of my code which would grow the
most is my len() function call, which would grow linearly as items are added to the dataset. 

## Task 1 

For Task 1, I used two for loops to add the unique numbers to their respective sets. 

The worst-case complexity for this algorithm would be O(n) because of the for loops and adding elements with a set. 
The reason for that is that since sets have no duplicates, adding a new element to a set requires a 
check to see if the element is already contained within the set.

This will grow proportionally as new items are added to the set. 

## Task 2 

For Task 2, I identified the phone record with the longest duration. 

My solution for this is O(n) since my code will run longer in a linear fashion (3x slower) as there
are three additional lines that would need to be processed and run with an additional item
added to the dataset. 

In this case, I needed to use Python's sorted algorithm, which uses timsort,
and has O(NlogN). I think the worst-case complexity of this would be O(n) for large datasets, and O(nlogN) for smaller ones since the O(n) runtime of my dataset would grow linearly as more items were added, but the O(nlogn) would grow pseduo-linearly and eventually be more efficient.

## Task 3

For Task 3, we were asked to find phone records and to calculate a percentage of calls called by records
from people in Bangalore. 

For this function, I used a recursive binary search to find the Bangalorean numbers. 

The complexity of this is O(NlogN), since there is an upfront cost to sort and format the phone records before
beginning the search process. Because the search uses a divide and conquer approach, it divides the list
in half which makes this very efficient. 

I initially tried an iterative approach to this problem, and it was slower to run than the recursive one. 

## Task 4

I worked with sets to find the similar and different numbers between different phone lists. 


I used sets to do unions and find differences. Because these data structures prevent duplicates,
union finds have O(n) runtime in some languages (not Python though), they are also ordered which
would make finds even more efficient. In this case, I needed to use Python's sorted algorithm, which uses timsort,
and has O(NlogN). I think the worst-case complexity of this would be O(n) for large datasets, and O(nlogN) for smaller ones since the O(n) runtime of my dataset would grow linearly as more items were added, but the O(nlogn) would grow pseduo-linearly and eventually be more efficient.