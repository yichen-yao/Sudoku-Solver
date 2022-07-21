# Sudoku Solver
# Yichen Yao


# sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



# for every three rows and columns, print a dividing line
def printBoard(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            # prints numbers on the board
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end= "")



# finds empty square denoted by 0 
def findEmpty(board):

    for i in range(len(board)): # scans row
        for j in range(len(board[0])): # scans column, board[0] = length of 1st list
            if board[i][j] == 0:
                return (i, j) # row, col
    
    return None


# as each number is entered into the empty position, checks if the current board is valid for sudoku.
# "position" is a tuple(row/column) 

# "number" is the value inserted
def valid(board, number, position):

    # scan and checks row; don't check current position
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # scan and checks column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # finds which box
    box_x = position[1]  // 3
    box_y = position[0] // 3

    # scans and checks boxes "0,1,2)". if in box 2, needs to multiple by 3 to get to index 6
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True 


def solve(board):

    # if the board is not empty, then we've solved the board
    find = findEmpty(board)
    if not find:
        return True   
    else:
        row, column = find

    # recursively solves the board
    for i in range(1,10):
        if valid(board, i, (row, column)):
            board[row][column] = i  # if valid, plugs into the board
            if solve(board): 
                return True

            # if position isn't valid, resets position and retrys process recursively
            board[row][column] = 0 
    
    return False

printBoard(board)
solve(board)
print("__________________________")
printBoard(board)
