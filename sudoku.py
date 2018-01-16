"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char grid

A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

[output] boolean

Return true if grid represents a valid Sudoku puzzle, otherwise return false.

"""
#My Solution:

def sudoku2(grid):

#check rows
    queue = []
    for i in grid:
        check_row = []
        for n in range(len(i)):
            if i[n] != '.':
                check_row.append(i[n])
        queue.append(check_row)
    for i in range(len(queue)):
        if len(queue[i]) < 2:
            continue
        else:
            check_row = set()
            for n in queue[i]:
                if n not in check_row:
                    check_row.add(n)
                    continue
                else:
                    return False
                    break
    #check columns
    switch_rows = []
    for i in range(len(grid)):
        new_row = []
        for n in grid:
            item = n[i]
            if item != '.':
                new_row.append(item)
        switch_rows.append(new_row)
    for i in range(len(switch_rows)):
        if len(switch_rows[i]) < 2:
            continue
        else:
            check_row = set()
            for n in switch_rows[i]:
                if n not in check_row:
                    check_row.add(n)
                    continue
                else:
                    return False
                    break
    #check subsquares
    def subsquare(index1,index2,index3,index4):
        subsquare = []
        for i in range(index1,index2):
            for n in range(index3,index4):
                if grid[i][n] != '.':
                    subsquare.append(grid[i][n])
        return subsquare

    def check_sub(sub):
        check = set()
        for i in sub:
            if i not in check:
                check.add(i)
                continue
            else:
                return False
                break
        return True

    sub1 = subsquare(0,3,0,3)
    check1 = check_sub(sub1)

    sub2 = subsquare(0,3,3,6)
    check2 = check_sub(sub2)

    sub3 = subsquare(0,3,6,9)
    check3 = check_sub(sub3)

    sub4 = subsquare(3,6,0,3)
    check4 = check_sub(sub4)

    sub5 = subsquare(3,6,3,6)
    check5 = check_sub(sub5)

    sub6 = subsquare(3,6,6,9)
    check6 = check_sub(sub6)

    sub7 = subsquare(6,9,0,3)
    check7 = check_sub(sub7)

    sub8 = subsquare(6,9,3,6)
    check8 = check_sub(sub8)

    sub9 = subsquare(6,9,6,9)
    check9 = check_sub(sub9)

    subsquares = [check1,check2,check3,check4,check5,check6,check7,check8,check9]
    for i in subsquares:
        if i == False:
            return False
            break
        else:
            continue
    return True
    
