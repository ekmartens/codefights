"""
Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.
"""
#My Solution:

def firstNotRepeatingCharacter(s):
    index = []
    count = {}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
            index.append(i)
    for n in index:
        if count[n] == 1:
            return n
    return "_"
