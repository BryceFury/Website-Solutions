'''

Codewars Kata - 8 Kyu - Sort and Star

Description:

You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

'''

def two_sort(array):
    return(''.join(''.join(letter + "***")  for letter in sorted(array)[0]))[:-3]