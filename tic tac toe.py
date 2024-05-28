from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    print("+-------+-------+-------+")
    for r in range(3):
        print("|       |       |       |")
        print("|", end="")
        for c in range(3):
            print("  ", board[r][c], end="   |")
        print("\n", end="")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    try:
        field = int(input("Enter your move: "))
        for r in range(3):
            for c in range(3):
                if board[r][c] == field:
                    board[r][c] = "O"
                    return
        raise Exception
    except:
        print("Please enter a valid number")
        enter_move(board)

def make_list_of_free_fields(board):
    global free_fields
    free_fields = []
    for r in range(3):
            for c in range(3):
                if type(board[r][c]) is int:
                    free_fields.append((r, c))

def victory_for(board, sign):
    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

def draw_move(board):
    make_list_of_free_fields(board)
    i = randrange(len(free_fields))
    r = free_fields[i][0]
    c = free_fields[i][1]
    board[r][c] = "X"

board[1][1] = "X"
while True:
    display_board(board)
    enter_move(board)
    display_board(board)
    draw_move(board)
    if victory_for(board, "O"):
        print("You won!")
        break
    if victory_for(board, "X"):
        display_board(board)
        print("The computer won!")
        break
    if len(free_fields) == 1:
        display_board(board)
        print("It's a draw!")
        break
