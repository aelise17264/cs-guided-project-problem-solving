"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    #given a string & want to return an intiger
    #keep a counter to keep track of number of vowels
    #we need to inspect every character in the input string
    #to see if it's a vowel but how do we know this?
    # doesn't look like there's a built-in function for this
    # keep a list or a string of all the vowels we are about
    # as we iterate we can check if the current character is part of the vowel string/list
    #if it is increment our counter
    #return our counter

    num_vowels = 0

    vowels = "aeiou"

    for char in input_str:
        if char in vowels:
            num_vowels += 1
    
    return num_vowels

print (get_count("abcdefghijklmnopqrstuvwxyz"))
