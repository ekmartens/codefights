"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i] ≤ 40.

[output] integer

The desired length.
"""
#My Solution:

def avoidObstacles(inputArray):
    obs = sorted(inputArray)
    full_lst = []

    for i in range(obs[-1]+2):
        full_lst.append(i)

    jump = 2
    o_s = True
    while o_s:
        o_s = False
        for i in range(len(full_lst)):
            if i == 0:
                pass
            if i%jump != 0:
                pass
            elif full_lst[i] in obs:
                jump+=1
                break
            if full_lst[i] != full_lst[-1]:
                continue
            else:
                return jump
        o_s = True
