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
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col

printBoard(board)
# print(len(board[0]))