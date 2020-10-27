"""
Challenge #1:

Write a function that retrieves the last n elements from a list.
we want the last x amount of digits
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    # Your code here
    # if n is longer than the length of the list it should return invalid
    # we need to return the last n elements as a list of ints
    #how would we do this is we just needed to return the first n elements?
    #we'd want to grab everything starting from index 0 up to n
    # we'd want to grab a subslice where that subslice starts at
    # the beginning of our input list has length n
    if n > len(a):
        return "invalid"
    last_n = a[len(a) -n:]
    return n
print (last([1, 2, 3, 4, 5], 1))
print ( last([4, 3, 9, 9, 7, 6], 3))
print (last([1, 2, 3, 4, 5], 7))
print (last([1, 2, 3, 4, 5], 0))
