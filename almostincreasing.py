"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""
#My Solution:

def almostIncreasingSequence(sequence):

    #initialize to false
    increase = False

    len_s = len(sequence)

    #check to see if the array has less than 3 items
    if len_s < 3:
        return True

    #check to see if the array is in an increasing sequence and the same length as the set version of the sequence no repeats - if yes, return True
    if sequence == sorted(sequence):
        if len_s == len(set(sequence)):
            return True

    increm = True
    for i in range(len_s):
        #if true AND the item is less than the length of sequence -1 AND the item is less than the next item, increm is still true, move on to the next block
        if increm and i < len_s-1 and sequence[i] < sequence[i+1]:
            increm = True
            continue
        #create a new sequence with the sequence up to the current item, then the rest of the sequence after the current item
        new_seq = sequence[:i] + sequence[i+1:]
        #if that new sequence is the same as the sequence in ascending order
        if new_seq == sorted(new_seq):
            #and also if the length of the new sequence is the same as the length of set version with no repeats, the overall return is now true, break the loop
            if len(new_seq) == len(set(new_seq)):
                increase = True
                break
        #if the above is not true, increm is now false, and so the loop ends leaving us with a return of false as at the start
        increm = False
    return increase
