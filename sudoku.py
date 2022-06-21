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



# as each number is entered into the empty position, checks if the current board
#  (row/column) is valid for sudoku.
#
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

printBoard(board)
# print(len(board[0]))