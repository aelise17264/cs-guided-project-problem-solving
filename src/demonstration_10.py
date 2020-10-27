"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    #given a string of numbers figure out the min & max
    # we have functions max & min built in
    # but these only work for numbers not strings
    # pass works on non negative numeric strings
    # b/c of negative numbers we can't get away w/ not turning the string into numbers
    # we need to transform it into a list of numbers, then we can use max & min
    str_digits = input_str.split(" ")
    int_digits = []

    for str_digit in str_digits:
        int_digit = int(str_digit)
        int_digits.append(int_digit)
    mx = max(int_digits)
    mn = min(int_digits)

    return f"{mx} {mn}"

print (max_and_min("1 2 3 4 5"))
print(max_and_min("1 9 3 4 -5"))
