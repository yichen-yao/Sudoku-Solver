

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

# prints sudoku board
def print_board(bo):

    # prints horizontal and vertical dividers every 3 rows and columns
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


# finds an empty spot(denoted by 0) and returns it
# returns row, column tuple
def find_empty(bo):
    for i in range(len(bo)):
        for i in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j )


# checks if the current board is valid for sudoku
def valid(bo, num, pos):

    # checks each row and see if # (tuple) is equal to num we just added in
    # ignores if position is the position we just inserted into
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1]!= i:
            return False

    # checks which box we are in
    # integer div to ensure its a whole number
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3)
        for j in range(box_x * 3, box_x * 3 + 3)
             if bo[i][j] == num and (i, j) != pos:
                 return False


# print_board(board)

