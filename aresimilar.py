"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""
#My Solution:

def areSimilar(a, b):

    if a == b:
        return True

    dif = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            dif += 1

    if dif < 2:
        return True
    elif dif == 2:
        if sorted(a) == sorted(b):
            return True
        else: return False
    else:
        return False
