"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""
#My Solution:

def palindromeRearranging(inputString):
        num_odd=0
        set_input=set(inputString)
        for i in set_input:
                x=inputString.count(i)
                if x%2!=0:
                        num_odd+=1
        return num_odd<=1
