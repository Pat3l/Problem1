# import numpy as np

N = 9  # N is the size of matrix

# A utility function to print grid...


def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


# Checks whether it will be legal to assign num to the given row, col..
def isSafe(grid, row, column, num):

    # This check if same number exits in a row or not.. if Yes it return false..
    for x in range(9):
        if grid[row][x] == num:
            return False

    # This check if same number exits in column or not.. if Yes it return false..
    for x in range(9):
        if grid[x][column] == num:
            return False

    # This checks for 3x3  square if same number exits or not as per sudoku laws..
    startRow = row - row % 3
    startColumn = column - column % 3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startColumn] == num:
                return False

    return True


'''
Takes a partially filled-in grid and attempts to assign values to all unassigned locations in
such a way to meet the requirements for Sudoku solution
(non-duplication across rows, columns, and boxes) */
'''


def solveSudoku(grid, row, column):
    '''
    Check if we have reached the 8th row and 9th column (0 indexed matrix) , we are
    returning true to avoid further backtracking
    '''
    if (row == (N-1) and column == N):
        return True

    # If column's value become 9.. it goes into next row and starts column from 0..
    if column == N:
        row += 1
        column = 0

    # if the value in grid is greater than 0.. we iterate for next column..
    if grid[row][column] > 0:
        return solveSudoku(grid, row, column+1)

    for num in range(1, N+1, 1):
        # This below function chcek if num(0-9) is safe to put in given row, column
        # then we move to next column...
        if isSafe(grid, row, column, num):
            # assigning the num in current position of grid.. assuming it is currect for the position..
            grid[row][column] = num

            # Checking the posibility with the next column..
            if solveSudoku(grid, row, column+1):
                return True

        # Removing the number as our assumption was wrong, and we go for next assumption with diffrent num value..
        grid[row][column] = 0
    return False


grid = [[0, 0, 0, 0, 0, 5, 0, 7, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 9],
        [5, 7, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 6, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 2, 3, 0, 6],
        [9, 0, 0, 5, 0, 7, 0, 0, 0],
        [7, 0, 0, 0, 0, 9, 0, 0, 5],
        [0, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 2, 8]]


if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution  exists ")
