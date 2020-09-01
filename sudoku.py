# Sudoku Solver


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
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j )
    return None # if no blank squares return None

# checks if the current board is valid for sudoku
def valid(bo, num, pos):

    # checks each row and see if # (tuple) is equal to num we just added in
    # ignores if position is the position we just inserted into
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # checks columns using same process
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # checks which box we are in; integer div to ensure its a whole number
    # box x/y outputs 0, 1, or 2. multiply by 3 to reach exact position
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

# works recursively
def solve(bo):

    find = find_empty(bo)
    if not find:
        return True # This is the final result we want
    else:
        row, col = find

    # loops through 1-9 and checks if i is valid solution
    # if its valid we add into the board
    # then recursively calls solve() until it finds correct solution
    # resets value to 0 if it can't be solved
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False

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

print_board(board)
print("########################")
solve(board)
print_board(board)